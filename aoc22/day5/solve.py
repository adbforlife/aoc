s = open('input', 'r').read().rstrip()
a,b = s.split('\n\n')
print(a)
crates = [[] for i in range(9)]
for l in a.split('\n')[:-1]:
    for i in range(9):
        j = 1 + i * 4
        if l[j] != ' ':
            crates[i].append(l[j])

for l in b.split('\n'):
    print(l)
    c,d,e,f,g,h = l.rstrip().split(' ')
    d = int(d)
    f = int(f)
    h = int(h)
    items = []
    for _ in range(d):
        item = crates[f - 1].pop(0)
        items.append(item)
    crates[h-1] = items + crates[h-1]
for c in crates:
    print(c[0])
print(crates)
