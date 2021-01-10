dat = open('input', 'r').read().rstrip().split('\n')
ds = ['E', 'S', 'W', 'N']
d = 0
pos = [1,10]
p = [0,0]
for r in dat:
    num = int(r[1:])
    if r[0] == 'N':
        pos[0] += num
    elif r[0] == 'S':
        pos[0] -= num
    elif r[0] == 'E':
        pos[1] += num
    elif r[0] == 'W':
        pos[1] -= num
    elif r[0] == 'L':
        if num // 90 == 1:
            pos[0],pos[1] = pos[1],-pos[0]
        elif num // 90 == 2:
            pos[0] *= -1
            pos[1] *= -1
        elif num // 90 == 3:
            pos[0],pos[1] = -pos[1],pos[0]
    elif r[0] == 'R':
        if num // 90 == 1:
            pos[0],pos[1] = -pos[1],pos[0]
        elif num // 90 == 2:
            pos[0] *= -1
            pos[1] *= -1
        elif num // 90 == 3:
            pos[0],pos[1] = pos[1],-pos[0]
    else:
        p[0] += num * pos[0]
        p[1] += num * pos[1]
        '''
        if d == 0:
            pos[1] += num
        elif d == 1:
            pos[0] -= num
        elif d == 2:
            pos[1] -= num
        else:
            pos[0] += num
        '''
print(abs(p[0]) + abs(p[1]))

