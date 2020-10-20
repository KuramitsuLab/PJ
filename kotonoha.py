import pegtree as pg
from pjcorpus import FUNCDATA

puppy_peg = pg.grammar('puppy2.tpeg')
puppy_parser = pg.generate(puppy_peg)

METHODS = {

}

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

    def stringfy(self, tree):
        backups = self.buffers
        self.buffers = []
        self.visit(tree)
        s = ''.join(self.buffers)
        self.buffers = backups
        return s

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
        fd = FUNCDATA[name] if name in FUNCDATA else {}
        p, p2 = self.params(tree.params, fd)
        self.pushFuncApp(name, p, fd, p2)
        
    def pushFuncApp(self, name, p, fd, p2=[]):
        #print('@', p)
        if 'stem' in fd:
            if len(p) in fd:
                params = fd[len(p)]
                self.push(params.format(*p))
            else:
                params = fd[1]
                self.push(params.format('と'.join(p)))
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

    # [#Infix left: [#Int '1']name: [#Name '+']right: [#Int '1']]
    def acceptInfix(self, tree):
        name = str(tree.name)
        p = [self.stringfy(tree.left), self.stringfy(tree.right)]
        self.pushFuncApp(name, p, FUNCDATA[name] if name in FUNCDATA else {})

    def acceptExpression(self, tree):
        self.visit(tree[0])

    # [#VarDecl left: [#Name 'a']right: [#List '[]']]
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
            self.push(f'{B}から{A}を取り出す')


transpiler = Transpiler()
print(transpiler.compile('a, b = c\nx,y = y,x'))
print(transpiler.compile('print("hello,world", end="")'))
print(transpiler.compile('print(i, fibo(1))'))

def pj(s):
    return transpiler.compile(s)

print(pj("a=1+1"))