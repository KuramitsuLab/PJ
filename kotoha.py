import pegtree as pg

puppy_peg = pg.grammar('puppy2.tpeg')
puppy_parser = pg.generate(puppy_peg)

METHODS = {

}

FUNCDATA = {
    'print': {
        'stem': '表示する',
        0: '空行を',
        1: '{}を',
        'end=': '{}を行末として',
        'end=""': '改行なしで',
        'seq=': '{}を区切り文字列として',
    },
    '+': {
        'stem': '加えた値',
        2: '{}を{}に',
    },
    '+=': {
        'stem': '増やす',
        2: '{}を{}だけ',
    }
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
    
    # [#Int 'a']
    def acceptInt(self, tree):
        self.push(str(tree))

    # [#QString 'a']
    def acceptQString(self, tree):
        self.push(str(tree))

    # [#Name 'a']
    def acceptName(self, tree):
        self.push(str(tree))

    # [#Data 'a']
    def acceptData(self, tree):
        self.push(str(tree))

    # [#ApplyExpr 'a']
    def acceptApplyExpr(self, tree):
        name = str(tree.name)
        fd = FUNCDATA[name] if name in FUNCDATA else {}
        p, p2 = self.params(tree.params, fd)
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
        
    def acceptExpression(self, tree):
        self.visit(tree[0])

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
                self.push(f'{A}を{BB}とする')
                self.push(f'{B}を{AA}とする')
        else:
            A = 'と'.join([self.stringfy(t) for t in tree.left.getSubNodes()])
            B = self.stringfy(tree.right)
            self.push(f'{B}から{A}を取り出す')


transpiler = Transpiler()
print(transpiler.compile('a, b = c\nx,y = y,x'))
print(transpiler.compile('print("hello,world", end="")'))
print(transpiler.compile('print(i, fibo(1))'))
