from parse import *
from collections import *
dat = open('input', 'r').read().rstrip().split('\n\n')
print(len(dat))
ts = []
for d in dat:
    rs = d.split('\n')
    num = parse("Tile {:d}:", rs[0])[0]
    rs = rs[1:]
    grid = [['0' for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if rs[i][j] == '#':
                grid[i][j] = '1'
    ts.append((num, grid))

print(ts[:2])
    

def get_ns(grid):
    s1 = ''.join(grid[0])
    s2 = ''.join(grid[-1])
    s3 = ''.join([grid[i][0] for i in range(10)])
    s4 = ''.join([grid[i][-1] for i in range(10)])
    ss = [s1,s2,s3,s4,s1[::-1], s2[::-1], s3[::-1], s4[::-1]]
    return list(map(lambda x : int(x, 2), ss))

cs = Counter()
for grid in ts:
    ns = get_ns(grid[1])
    for n in ns:
        cs[n] += 1

res = 1
for grid in ts:
    ns = get_ns(grid[1])
    cnt = 0
    for n in ns:
        if cs[n] == 1:
            cnt += 1
    if cnt == 4:
        res *= grid[0]

def rot(grid):
    res = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            res[i][j] = res[10-j][i]
    return res

def flip(grid):
    res = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            res[i][j] = res[i][10-j]
    return res

for grid in ts:
    if grid[0] == 1327:
        ns = get_ns(grid[1])
        n1,n2 = ns[0],ns[2]
        
        print(cs[n])





m = {}
res = [[-1 for _ in range(12)] for _ in range(12)]
res[0][0] = 1327
for grid in ts:
    ns = get_ns(grid[1])
    for n in ns:
        
