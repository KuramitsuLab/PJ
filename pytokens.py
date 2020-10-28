import sys
import pegtree as pg

METHODS = {

}

class Tokenizer(object):
    buffers: list
    parser: object
    def __init__(self, grammar='puppy2.tpeg'):
        self.buffers = []
        peg = pg.grammar(grammar)
        self.parser = pg.generate(peg)

    def push(self, s):
        self.buffers.append(s)

    def compile(self, source):
        tree = self.parser(source)
        self.buffers = []
        self.visit(tree)
        return self.buffers
    
    def visit(self, tree):
        tag = tree.getTag()
        if tag not in METHODS:
            METHODS[tag] = f'accept{tag}'
        method = METHODS[tag]
        if hasattr(self, method):
            method = getattr(self, method)
            return method(tree)
        else:
            print('@TODO', repr(tree))
            self.push(str(tree))

    def pushTrees(self, tree, start='(', sep=',', end=')'):
        if start != '':
            self.push(start)
        if len(tree) > 0:
            trees = tree.getSubNodes()
            for t in trees[:-1]:
                self.visit(t)
                self.push(sep)
            self.visit(trees[-1])
        if end != '':
            self.push(end)

    def acceptSource(self, tree):
        self.pushTrees(tree, '', '[SEP]', '')

    def acceptBlock(self, tree):
        self.pushTrees(tree, '[BGN]', '[SEP]', '[END]')

    def acceptTrueExpr(self, tree):
        self.push('True')

    def acceptFalseExpr(self, tree):
        self.push('False')

    def acceptInt(self, tree):
        self.push(str(tree))

    def acceptFloat(self, tree):
        self.push(str(tree))

    def acceptDouble(self, tree):
        self.push(str(tree))

    # [#QString 'a']
    def acceptQString(self, tree):
        self.push(str(tree))

    # [#Name 'a']
    def acceptName(self, tree):
        self.push(str(tree))

    # [#Tuple 'a']
    def acceptTuple(self, tree):
        if len(tree) == 1:
            self.visit(tree[0])
        else:
            self.pushTrees(tree, '(', ',', ')')

    # [#List 'a']
    def acceptList(self, tree):
        if len(tree) == 0:
            self.push('[]')
        else:
            self.pushTrees(tree, '[', ',', ']')

    # [#Data 'a']
    def acceptData(self, tree):
        self.push(str(tree))

    # [#ApplyExpr 'a']
    def acceptApplyExpr(self, tree):
        name = str(tree.name)
        self.push(name)
        self.pushTrees(tree.params)

    # [#MethodExpr 'a']
    def acceptMethodExpr(self, tree):
        self.visit(tree.recv)
        self.push('.')
        name = str(tree.name)
        self.push(name)
        self.pushTrees(tree.params)

    # [#IndexExpr 'a']
    def acceptIndexExpr(self, tree):
        self.visit(tree.recv)
        self.push('[')
        self.visit(tree.index)
        self.push(']')

    # [#Infix left: [#Int '1']name: [#Name '+']right: [#Int '1']]
    def acceptUnary(self, tree):
        name = str(tree.name)
        self.push(name)
        self.visit(tree.expr)

    # [#Infix left: [#Int '1']name: [#Name '+']right: [#Int '1']]
    def acceptInfix(self, tree):
        name = str(tree.name)
        self.visit(tree.left)
        self.push(name)
        self.visit(tree.right)

    def acceptMul(self, tree):
        self.visit(tree[0])
        self.push('*')
        self.visit(tree[1])

    def acceptAnd(self, tree):
        self.visit(tree.left)
        self.push('and')
        self.visit(tree.right)

    def acceptOr(self, tree):
        self.visit(tree.left)
        self.push('or')
        self.visit(tree.right)

    def acceptNot(self, tree):
        self.push('not')
        self.visit(tree[0])

    def acceptIfExpr(self, tree):
        self.visit(tree.get('then'))
        self.push('if')
        self.visit(tree.cond)
        self.push('else')
        self.visit(tree.get('else'))

    def acceptExpression(self, tree):
        self.visit(tree[0])

    # a = []    [#VarDecl left: [#Name 'a']right: [#List '[]']]
    def acceptVarDecl(self, tree):
        self.visit(tree.left)
        self.push('=')
        self.visit(tree.right)

    # a,b = c [#MultiAssignment left: [# [#Name 'a'][#Name 'b']]right: [#Name 'c']]
    def acceptMultiAssignment(self, tree):
        self.pushTrees(tree.left, '', ',', '')
        self.push('=')
        if len(tree.right) == 1:
            self.visit(tree.right)
        else:
            self.pushTrees(tree.right, '', ',', '')

    # a += 1
    def acceptSelfAssignment(self, tree):
        name = str(tree.name)
        self.visit(tree.left)
        self.push(name)
        self.visit(tree.right)

    # a = 1
    def acceptAssignment(self, tree):
        self.visit(tree.left)
        self.push('=')
        self.visit(tree.right)

    # if a > 0: pass
    def acceptPass(self, tree):
        self.push('pass')

    # if a > 0: pass
    def acceptIf(self, tree):
        self.push('if')
        self.visit(tree.cond)
        self.push(':')
        self.visit(tree.get('then'))
        if tree.has('elif'):
            for t in tree.get('elif').getSubNodes():
                self.visit(t)
        if tree.has('else'):
            self.push('else')
            self.push(':')
            self.visit(tree.get('else'))

    def acceptElif(self, tree, ):
        self.push('elif')
        self.visit(tree.cond)
        self.push(':')
        self.visit(tree.get('then'))

    def acceptWhile(self, tree):
        self.push('while')
        self.visit(tree.cond)
        self.push(':')
        self.visit(tree.body)

    def acceptFor(self, tree):
        self.push('for')
        self.pushTrees(tree.each, '', ',', '')
        self.push('in')
        self.visit(tree.list)
        self.push(':')
        self.visit(tree.body)

    def acceptListForExpr(self, tree):
        self.push('[')
        self.visit(tree.append)
        for t in tree:
            self.push('for')
            self.visit(t.each)
            self.push('in')
            self.visit(t.list)
            if t.has('cond'):
                self.push('if')
                self.visit(t.cond)
        self.push(']')

    # break
    def acceptBreak(self, tree):
        self.push('break')

    # continue
    def acceptContinue(self, tree):
        self.push('continue')

    # def f(a,b):
    def acceptFuncDecl(self, tree):
        self.push('def')
        name = str(tree.name)
        self.push(name)
        self.pushTrees(tree.params)
        self.push(':')
        self.visit(tree.body)

    # return
    def acceptReturn(self, tree):
        self.push('return')
        if tree.has('expr'):
            self.visit(tree.expr)

    def acceptImportDecl(self, tree):
        self.push('import')
        name = str(tree.name)
        self.push(name)



#tokenizer = Tokenizer()
#print(transpiler.compile('a, b = c\nx,y = y,x'))
#print(transpiler.compile('print("hello,world", end="")'))
#print(transpiler.compile('print(i, fibo(1))'))

if __name__ == '__main__':
    tokenizer = Tokenizer()
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            print(tokenizer.compile(f.read()))
