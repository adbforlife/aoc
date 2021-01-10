from itertools import product
dat = open('input', 'r').read().rstrip().split('\n')
d = [[0 for _ in range(20)] for _ in range(20)]
for i in range(len(dat)):
    r = dat[i]
    gg = [0 for _ in range(6)]
    for c in r:
        if c == '#':
            gg.append(1)
        else:
            gg.append(0)
    gg += [0 for _ in range(6)]
    print(gg)
    d[i+6] = gg
dat = [[[[0 for _ in range(20)] for _ in range(20)] for _ in range(20)] for _ in range(20)]
dat[10][10] = d

def ok(d,i,j,k,l):
    return i >= 0 and j >= 0 and k >= 0 and l >= 0 and i < len(d) and j < len(d) and k < len(d) and l < len(d)

def num_n(d,i,j,k,l):
    cnt = 0
    for i2,j2,k2,l2 in product([-1,0,1], repeat=4):
        if (i2,j2,k2,l2) != (0,0,0,0):
            i3,j3,k3,l3 = i+i2,j+j2,k+k2,l+l2
            if ok(d,i3,j3,k3,l3):
                if d[i3][j3][k3][l3]:
                    cnt += 1
    return cnt

for n in range(6):
    newdat = [[[[0 for _ in range(20)] for _ in range(20)] for _ in range(20)] for _ in range(20)]
    for i in range(20):
        for j in range(20):
            for k in range(20):
                for l in range(20):
                    num = num_n(dat,i,j,k,l)
                    if dat[i][j][k][l] == 1:
                        if num == 2 or num == 3:
                            newdat[i][j][k][l] = 1
                        else:
                            newdat[i][j][k][l] = 0
                    else:
                        if num == 3:
                            newdat[i][j][k][l] = 1
                        else:
                            newdat[i][j][k][l] = 0
    dat = newdat

def counts(d):
    cnt = 0
    for i in range(20):
        for j in range(20):
            for k in range(20):
                for l in range(20):
                    cnt += d[i][j][k][l]
    return cnt
print(counts(dat))

