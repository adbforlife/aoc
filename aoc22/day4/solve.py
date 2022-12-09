s = open('input', 'r').read().rstrip().split('\n')
res = 0
for l in s:
    l = l.rstrip()
    a,b = l.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    print(a1,a2,b1,b2)
    add = True
    if a2 < b1 or b2 < a1:
        add = False
    if add:
        res += 1

print(res)
