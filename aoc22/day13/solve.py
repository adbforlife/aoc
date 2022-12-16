from functools import cmp_to_key
from copy import deepcopy
s = open('input', 'r').read().rstrip()
s = s.split('\n\n')
res = 0


def check(a,b):
    if len(a) == 0 and len(b) == 0:
        return -1
    if len(a) == 0:
        return 1
    if len(b) == 0:
        return 0
    if type(a[0]) == type(0) and type(b[0]) == type(0):
        if a[0] < b[0]:
            return 1
        elif a[0] > b[0]:
            return 0
        else:
            a.pop(0)
            b.pop(0)
            return check(a,b)
    elif type(a[0]) == type(0):
        a[0] = [a[0]]
        return check(a,b)
    elif type(b[0]) == type(0):
        b[0] = [b[0]]
        return check(a,b)
    else:
        truth = check(a[0], b[0])
        if truth != -1:
            return truth
        a.pop(0)
        b.pop(0)
        return check(a,b)
def check_real(a,b):
    c = deepcopy(a)
    d = deepcopy(b)
    v = check(c,d)
    if v == 0:
        return 1
    return -1

ls = []

for i in range(len(s)):
    l = s[i].rstrip()
    a,b = l.split('\n')
    a = eval(a)
    b = eval(b)
    ls.append(a)
    ls.append(b)

res = 1
ls.append([[2]])
ls.append([[6]])
for l in ls:
    print(l)

print('---')
ls2 = sorted(ls, key=cmp_to_key(check_real))
for i in range(len(ls2)):
    l = ls2[i]
    print(l)
    if len(l) == 1 and ( str(l[0]) == '[2]' or str(l[0]) == '[6]'):
        res *= i+1

print(res)
