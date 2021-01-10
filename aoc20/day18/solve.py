dat = open('input', 'r').read().rstrip().split('\n')
gg = 0
for r in dat:
    stack = []
    for tok in r.split():
        if tok == '+' or tok == '*':
            stack.append(tok)
            continue
        while tok[0] == '(':
            tok = tok[1:]
            stack.append('(')
        n = tok.split(')')[0]
        if len(stack) == 0 or stack[-1] == '(':
            stack.append(n)
        else:
            res = eval(stack[-2] + stack[-1] + n)
            stack.pop()
            stack.pop()
            stack.append(str(res))
        for _ in range(len(tok) - len(n)):
            stack.pop(-2)
            while len(stack) > 1 and stack[-2] != '(':
                res = eval(stack.pop() + stack.pop() + stack.pop())
                stack.append(str(res))
    assert(len(stack) == 1)
    gg += int(stack[0])
print(gg)

from functools import *
from infix import *

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)
    def __mod__(self, other):
        return self.func(other)
@mod_infix
def gg(x,y):
    return x + y

@or_infix
def bb(x,y):
    return x * y

res = 0
for r in dat:
    r = r.replace('*', '|bb|')
    r = r.replace('+', '%gg%')
    print(r)
    res += eval(r)
print(res)
