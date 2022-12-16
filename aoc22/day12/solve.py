s = open('input', 'r').read().rstrip()
s = s.split('\n')
alph = 'abcdefghijklmnopqrstuvwxyz'
m = [[] for _ in range(len(s))]
steps = [[] for _ in range(len(s))]
start = (-1, -1)
end = (-1, -1)
for i in range(len(s)):
    l = s[i]
    for j in range(len(l.rstrip())):
        c = l[j]
        if c in alph:
            m[i].append(alph.index(c))
            steps[i].append(-1)
        else:
            assert(c == 'E' or c == 'S')
            steps[i].append(0)
            if c == 'S':
                m[i].append(0)
                start = (i, j)
            else:
                m[i].append(-1)
                end = (i, j)

print(start, end)

def neighbors(n):
    res = []
    i,j = n
    val = m[i][j]
    cands = [(i-1, j), (i + 1, j), (i, j-1), (i, j+1)]
    for cand in cands:
        a,b = cand
        if a < 0 or b < 0 or a >= len(m) or b >= len(m[0]):
            continue
        elif m[a][b] > val + 1:
            continue
        res.append(cand)
    return res


def calc(start):
    steps = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    added = set([])
    added.add(start)
    bag = [start]
    while len(bag) > 0:
        n = bag.pop(0)
        i,j = n
        ns = neighbors(n)
        for node in ns:
            if node in added:
                continue
            bag.append(node)
            added.add(node)
            a,b = node
            steps[a][b] = steps[i][j] + 1
    return steps[end[0]][end[1]]

best = 1000
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 0:
            start = i,j
            candidate = calc(start)
            print(start, candidate)
            if candidate > 0:
                best = min(best, candidate)
print(best)

