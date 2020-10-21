import pegtree as pg
from pjcorpus import get_corpus

puppy_peg = pg.grammar('puppy2.tpeg')
puppy_parser = pg.generate(puppy_peg)

METHODS = {

}

def chunk(s, fmt='{{%}}'):
    nested = 0
    found = False
    for i in range(len(s)):
        if s.startswith("{{", i):
            nested += 1
        elif s.startswith("}}", i):
            nested -= 1
        elif nested == 0 and s[i] in "にをがで":
            found = True
            break
    if found:
        return fmt.replace('%', s)
    return s

class Transpiler(object):
    buffers: list
    def __init__(self):
        self.buffers = []

    def push(self, s):
        self.buffers.append(s)

    def pushLF(self):
        self.buffers.append('\n')

    def compile(self, source):
        tree = puppy_parser(source)
        self.buffers = []
        self.visit(tree)
        return ''.join(self.buffers)
    
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
            self.push(repr(tree))

    def stringfy(self, tree, fmt='{{%}}'):
        backups = self.buffers
        self.buffers = []
        self.visit(tree)
        s = ''.join(self.buffers)
        self.buffers = backups
        return chunk(s, fmt)

    def acceptSource(self, tree):
        if len(tree) == 1:
            self.visit(tree[0])
        else:
            for t in tree.getSubNodes():
                self.visit(t)
                self.pushLF()
    
    def acceptInt(self, tree):
        self.push(str(tree))

    def acceptFloat(self, tree):
        self.push(str(tree))

    # [#QString 'a']
    def acceptQString(self, tree):
        self.push(str(tree))

    # [#Name 'a']
    def acceptName(self, tree):
        name = str(tree)
        fd = get_corpus(name)
        if 'name' in fd:
            self.push(fd['name'])
        else:
            self.push(str(tree))

    # [#List 'a']
    def acceptList(self, tree):
        if len(tree) == 0:
            self.push('空のリスト')
        else:
            ','.join([self.stringfy(t) for t in tree.getSubNodes()])
            self.push('のリスト')

    # [#Data 'a']
    def acceptData(self, tree):
        self.push(str(tree))

    # [#ApplyExpr 'a']
    def acceptApplyExpr(self, tree):
        name = str(tree.name)
        fd = get_corpus(name)
        p, p2 = self.params(tree.params, fd)
        self.pushFuncApp(name, p, fd, p2)
        
    def pushFuncApp(self, name, p, fd, p2=[]):
        #print('@', p)
        if len(fd) > 0:
            if len(p) in fd:
                params = fd[len(p)]
                self.push(params.format(*p))
            else:
                params = fd[1]
                self.push(params.format('と'.join(p)))
            if 'stem' in fd:
                for c in p2:
                    self.push(c)
                self.push(fd['stem'])
        else:
            params = ','.join(p)
            self.push(f'{name}({params})') 
    
    def params(self, params, fd):
        p = []
        p2=[]
        for tree in params.getSubNodes():
            #print(repr(tree), f'{tree[0].name}' if len(tree) > 0 else '@')
            if tree.getTag() == 'Data' and len(tree) > 0 and f'{tree[0].name}=' in fd:
                for t in tree.getSubNodes():
                    key = str(t.name)+'='
                    keyval = key+str(t.value).replace("'", '"')
                    if keyval in fd:
                        p2.append(fd[keyval])
                    elif key in fd:
                        p2.append(fd[key].format(self.stringfy(t.value)))
            else:
                p.append(self.stringfy(tree))
        return p, p2

    # [#MethodExpr 'a']
    def acceptMethodExpr(self, tree):
        recv = self.stringfy(tree.recv)
        name = str(tree.name)
        fd = get_corpus(f'.{name}', recv)
        p, p2 = self.params(tree.params, fd)
        p = [recv] + p
        self.pushFuncApp(name, p, fd, p2)

    # [#IndexExpr 'a']
    def acceptIndexExpr(self, tree):
        recv = self.stringfy(tree.recv)
        index = self.stringfy(tree.index)
        if index == '0':
            self.push(f'{recv}の先頭')
        elif index == '-':
            self.push(f'{recv}の末尾')
        else:
            self.push(f'{recv}の{index}番目')

    # [#Infix left: [#Int '1']name: [#Name '+']right: [#Int '1']]
    def acceptUnary(self, tree):
        name = str(tree.name)
        p = [self.stringfy(tree.expr)]
        self.pushFuncApp(name, p, get_corpus(name))

    # [#Infix left: [#Int '1']name: [#Name '+']right: [#Int '1']]
    def acceptInfix(self, tree):
        name = str(tree.name)
        p = [self.stringfy(tree.left), self.stringfy(tree.right)]
        self.pushFuncApp(name, p, get_corpus(name))

    def acceptAnd(self, tree):
        p = [self.stringfy(tree.left), self.stringfy(tree.right)]
        self.push(f'{p[0]}、かつ{p[1]}')

    def acceptOr(self, tree):
        p = [self.stringfy(tree.left), self.stringfy(tree.right)]
        self.push(f'{p[0]}、または{p[1]}')

    def acceptNot(self, tree):
        p = [self.stringfy(tree.expr)]
        self.push(f'{p[0]}の反対')


    def acceptExpression(self, tree):
        self.visit(tree[0])

    # a = []    [#VarDecl left: [#Name 'a']right: [#List '[]']]
    def acceptVarDecl(self, tree):
        A = self.stringfy(tree.left) 
        B = self.stringfy(tree.right)
        self.pushLet(A, B)

    def pushLet(self, A, B):
        self.push(f'{A}を{B}とする')

    # a,b = c [#MultiAssignment left: [# [#Name 'a'][#Name 'b']]right: [#Name 'c']]
    def acceptMultiAssignment(self, tree):
        if len(tree.left) == 2 and len(tree.right) == 2:
            A = self.stringfy(tree.left[0])
            B = self.stringfy(tree.left[1])
            AA = self.stringfy(tree.right[0])
            BB = self.stringfy(tree.right[1])
            if A == BB and B == AA:
                self.push(f'{A}と{B}を入れ替える')
            else:
                self.pushLet(A,BB)
                self.pushLet(B,AA)
        else:
            A = 'と'.join([self.stringfy(t) for t in tree.left.getSubNodes()])
            B = self.stringfy(tree.right)
            self.push(f'{B}を順番に取り出して{A}とする')

    # a += 1
    def acceptSelfAssignment(self, tree):
        name = str(tree.name)
        p = [self.stringfy(tree.left), self.stringfy(tree.right)]
        self.pushFuncApp(name, p, get_corpus(name))

    # if a > 0: pass
    def acceptPass(self, tree):
        self.push(f'何もしない')

    # if a > 0: pass
    def acceptIf(self, tree):
        cond = self.stringfy(tree.cond, fmt='%')
        self.push(f'もし{cond}のとき、')
        self.pushBlock(tree.get('then'))
        if 'else' in tree:
            self.pushLF()
            self.push(f'そうでなければ、')
            self.pushBlock(tree.get('else'))

    def acceptWhile(self, tree):
        cond = self.stringfy(tree.cond, fmt='%')
        self.push(f'もし{cond}のとき、')
        self.pushBlock(tree.body, 'ことを繰り返す')

    def pushBlock(self, tree, suffix=''):
        self.visit(tree[0])
        self.push(suffix)

transpiler = Transpiler()
print(transpiler.compile('a, b = c\nx,y = y,x'))
print(transpiler.compile('print("hello,world", end="")'))
print(transpiler.compile('print(i, fibo(1))'))

def pj(s):
    return transpiler.compile(s)

print(pj("a+=-1"))

print(pj("counter=0"))
print(pj("while counter <=10 and a[0] >=0 : counter += 1"))

print(pj("if x < y : pass"))
print(pj("a,b,c =map(int, input().split())"))