from parse import *
dat = open('input2', 'r').read().rstrip().split('\n\n')
rs = dat[0].split('\n')
rs2 = []
for r in rs:
    a,b = r.split(': ')
    a = int(a)
    if '"' in b:
        rs2.append((a, b.replace('"', '')))
    elif parse("{:d}", b):
        p = parse("{:d}", b)
        rs2.append((a, p[0]))
    elif parse("{:d} {:d}", b):
        p = parse("{:d} {:d}", b)
        rs2.append((a, p[0], p[1]))
    elif parse("{:d} | {:d}", b):
        p = parse("{:d} | {:d}", b)
        rs2.append((a, p[0]))
        rs2.append((a, p[1]))
    elif parse("{:d} {:d} | {:d} {:d}", b):
        p = parse("{:d} {:d} | {:d} {:d}", b)
        rs2.append((a, p[0], p[1]))
        rs2.append((a, p[2], p[3]))
    elif parse("{:d} | {:d} {:d}", b):
        p = parse("{:d} | {:d} {:d}", b)
        rs2.append((a, p[0]))
        rs2.append((a, p[1], p[2]))
    elif parse("{:d} {:d} | {:d} {:d} {:d}", b):
        p = parse("{:d} {:d} | {:d} {:d} {:d}", b)
        rs2.append((a, p[0], p[1]))
        rs2.append((136, p[2], p[3]))
        rs2.append((a, 136, p[4]))
    else:
        print(b)
        assert(0)

rs = []
for r in rs2:
    if type(r[1]) == str:
        rs.append(r)
        continue
    if len(r) == 2:
        for k in rs2:
            if k[0] == r[1]:
                if len(k) == 2:
                    rs.append((r[0], k[1]))
                else:
                    rs.append((r[0], k[1], k[2]))
    else:
        rs.append(r)

ss = dat[1].split('\n')
def match(s):
    n = len(s)
    P = [[[0 for _ in range(len(rs2))] for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for r in rs:
            if r[1] == s[i]:
                P[1][i][r[0]] = 1
    
    for i in range(2, n+1):
        for j in range(n-i+1):
            for k in range(1, i):
                for r in rs:
                    if len(r) == 2:
                        continue
                    if P[k][j][r[1]] and P[i-k][j+k][r[2]]:
                        P[i][j][r[0]] = 1
    return P[n][0][0]

cnt = 0
print(len(ss))
for i in range(len(ss)):
    print(i)
    cnt += match(ss[i])
    print(cnt)
print(cnt)
