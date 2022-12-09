s = open('input', 'r').read().rstrip().split('\n')
assert(len(s) == 2500)
d1 = {'A': 1, 'B': 2, 'C': 3}
d2 = {'X': -1, 'Y': 0, 'Z': 1}
res = 0
for l in s:
    a,b = l.rstrip().split(' ')
    a = d1[a]
    b = d2[b]
    if b == -1:
        c = a - 1
        if c == 0:
            c = 3
    elif b == 0:
        c = a
    else:
        c = a + 1
        if c == 4:
            c = 1

    toadd = c
    if a == c:
        toadd += 3
    elif c - a == 1 or c - a == -2:
        toadd += 6
    else:
        toadd += 0
    print(toadd)
    res += toadd
print(res)
