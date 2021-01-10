import sys
from copy import *
sys.setrecursionlimit(100000)
dat1, dat2 = open('input', 'r').read().rstrip().split('\n\n')
dat1 = dat1.split('\n')[1:]
dat2 = dat2.split('\n')[1:]
dat1 = list(map(int, dat1))
dat2 = list(map(int, dat2))

def round(dat1, dat2):
    n1 = dat1.pop(0)
    n2 = dat2.pop(0)
    if n1 <= len(dat1) and n2 <= len(dat2):
        return (n1, n2, 1)
    if n1 > n2:
        dat1.append(n1)
        dat1.append(n2)
    else:
        dat2.append(n2)
        dat2.append(n1)
    return 0

def compute(dat1, dat2):
    res = 0
    if len(dat1) > 0 and len(dat2) > 0:
        for i in range(1, len(dat1)+1):
            res += dat1[-i] * i
        return (1,res)
    dat = dat1 + dat2
    for i in range(1, len(dat)+1):
        res += dat[-i] * i
    if dat1:
        return (1,res)
    else:
        return (2, res)

mem = {}
maxboi = 0
def game(dat1, dat2):
    d1 = tuple(dat1)
    d2 = tuple(dat2)
    if (d1, d2) in mem:
        res = mem[(d1, d2)]
        if res == -1:
            res = compute(d1, d2)
            mem[(d1, d2)] = res
        return res
    else:
        mem[(d1, d2)] = -1
    if len(d1) == 0 or len(d2) == 0:
        mem[(d1, d2)] = compute(d1, d2)
        return mem[(d1, d2)]
    round_res = round(dat1, dat2)
    if len(dat1) + len(dat2) >= 44:
        print(len(mem), len(dat1), len(dat2))
    if not round_res:
        res = game(dat1, dat2)
        mem[(d1, d2)] = res
        return res
    else:
        n1,n2 = round_res[0], round_res[1]
        sub_res = game(copy(dat1[:n1]), copy(dat2[:n2]))
        if sub_res[0] == 1:
            dat1.append(n1)
            dat1.append(n2)
        else:
            dat2.append(n2)
            dat2.append(n1)
        res = game(dat1, dat2)
        mem[(d1, d2)] = res
        return res
        
res = game(dat1, dat2)
print(res)

cnt = 0
for m in mem:
    if len(m[0]) + len(m[1]) == 10:
        cnt += 1
print(cnt)


