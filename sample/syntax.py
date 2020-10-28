# Python Syntax

class Cls:
    x = 3             # class variable
inst = Cls()
inst.x = inst.x + 1   # writes inst.x as 4 leaving Cls.x as 3

def f(arg): pass    # a function that does nothing (yet)

class C: pass       # a class with no methods (yet)

try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened") from exc