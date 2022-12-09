s = open('input', 'r').read().rstrip()
ls = s.split('\n')
m = []
for l in ls:
    l = list(map(int, l.rstrip()))
    m.append(l)

best = 0
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if i == 0 or i == len(ls) - 1:
            pass
        elif j == 0 or j == len(ls[0]) - 1:
            pass
        else:
            v = m[i][j]
            s1 = i
            for a in range(0, i):
                if m[a][j] >= v:
                    s1 = i - a
            s2 = len(ls) - 1 - i
            for a in range(i+1, len(ls))[::-1]:
                if m[a][j] >= v:
                    s2 = a - i
            s3 = j
            for a in range(0, j):
                if m[i][a] >= v:
                    s3 = j - a
            s4 = len(ls[0]) - 1 - j
            for a in range(j+1, len(ls[0]))[::-1]:
                if m[i][a] >= v:
                    s4 = a - j
            s = s1 * s2 * s3 * s4
            best = max(s, best)
print(best)
