dat = open('input', 'r').read().rstrip().split('\n')
dat = list(map(int, dat))
bad = 0
curr = 0
pres = []
for i in range(len(dat)):
    pres.append(curr)
    curr += dat[i]
pres.append(curr)
for i in range(25, len(dat)):
    gg = False
    for j in range(i-25, i):
        for k in range(i-25, i):
            if j != k and dat[j] + dat[k] == dat[i]:
                gg = True
    if not gg:
        print(i)
        bad = i
        print(dat[i])
        break
        exit(0)

for i in range(bad-2):
    for j in range(i, bad+1):
        if pres[j] - pres[i] == dat[bad]:
            print('ya')
            gg = [dat[k] for k in range(i,j)]
            print(max(gg) + min(gg))
            exit(0)

'''
bads = [0,1]
pres = []
curr = 0
for i in range(len(dat)):
    pres.append(curr)
    curr += dat[i]
pres.append(curr)
for i in range(2, len(dat)):
    gg = False
    for j in range(i-2):
        for k in range(j+2,i+1):
            if pres[k] - pres[j] == dat[i]:
                gg = True
                break
        if gg:
            break
    if not gg:
        print(i)
        bads.append(i)
bads = list(map(lambda x: dat[x], bads))
print(max(bads), min(bads))
'''
'''
for i in range(25, len(dat)):
    gg = False
    for j in range(i-25, i):
        for k in range(i-25, i):
            if j != k and dat[j] + dat[k] == dat[i]:
                gg = True
    if not gg:
        print(i)
        print(dat[i])
        exit(0)
'''
