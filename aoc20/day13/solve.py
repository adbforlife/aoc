dat = open('input', 'r').read().rstrip().split('\n')
ts = int(dat[0])
dat = dat[1]
dat = dat.split(',')
mods = []
newdat = []
for i in range(len(dat)):
    if dat[i] != 'x':
        mods.append(i)
        newdat.append(int(dat[i]))
print(mods)
print(newdat)
p = 1
for d in newdat:
    p *= d
Ms = list(map(lambda x: p // x, newdat))
Ms 
'''
dat = list(filter(lambda x: x != 'x', dat))
dat = list(map(int, dat))
best = 2000000
bus = 0
for n in dat:
    print(n)
    curr = (ts + (n - 1)) // n * n - ts
    if curr < best:
        best = curr
        bus = n

print(bus * best)
'''
