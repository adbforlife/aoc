from itertools import *
dat = open('input', 'r').read().rstrip().split('\n')
mask = ''
mask0 = 0
mask1 = 0
mem = {}
#mem = [0 for _ in range(1000000)]
for r in dat:
    if r[:3] == "mas":
        mask = r.split(' = ')[1]
        mask0 = list(map(lambda x: '0' if x == '0' else '1', mask))
        mask0 = int(''.join(mask0), 2)
        mask1 = list(map(lambda x: '1' if x == '1' else '0', mask))
        mask1 = int(''.join(mask1), 2)
    else:
        num = r.split(' = ')[1]
        num = int(num)
        pos = r.split('[')[1].split(']')[0]
        pos = bin(int(pos))[2:].rjust(36, '0')
        for a in product([0,1],repeat=mask.count('X')):
            newpos = []
            cnt = 0
            for i in range(len(mask)):
                if mask[i] == 'X':
                    newpos.append(str(a[cnt]))
                    cnt += 1
                elif mask[i] == '1':
                    newpos.append('1')
                elif mask[i] == '0':
                    newpos.append(pos[i])
            newpos = int(''.join(newpos), 2)
            mem[newpos] = num

tot = 0
for k in mem:
    tot += mem[k]
print(tot)
