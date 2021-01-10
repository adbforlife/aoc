dat = open('input', 'r').read().rstrip().split('\n')
dat = list(map(int, dat))
dat = sorted(dat)
res = [-1 for _ in range(len(dat))]
res[-1] = 1
res[-2] = 1
res[-3] = 2
start = 0
for i in range(len(dat)-3)[::-1]:
    if dat[i+1] - dat[i] == 3:
        res[i] = res[i+1]
    else:
        if dat[i+2] - dat[i] == 4:
            res[i] = res[i+1]
        elif dat[i+3] - dat[i] == 5:
            res[i] = res[i+1] + res[i+2]
        else:
            res[i] = res[i+1] + res[i+2] + res[i+3]
print(res[0] + res[1])
print(dat)
print(threes, ones)
threes += 1
print(threes * ones)
print(len(dat) + 1)
