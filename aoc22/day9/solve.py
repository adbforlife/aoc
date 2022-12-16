s = open('input', 'r').read().rstrip()
s = s.split('\n')
ps = [(0,0) for _ in range(10)]
pos = set([])
pos.add((0,0))

def update(q1, q2):
    d0 = abs(q1[0] - q2[0])
    d1 = abs(q1[1] - q2[1])
    if d0 <= 1 and d1 <= 1:
        return q2
    elif d0 == 0:
        return (q2[0], q2[1] + 1 if q2[1] < q1[1] else q2[1] - 1)
    elif d1 == 0:
        return (q2[0] + 1 if q2[0] < q1[0] else q2[0] - 1, q2[1])
    else:
        x = q2[0] + 1 if q2[0] < q1[0] else q2[0] - 1
        y = q2[1] + 1 if q2[1] < q1[1] else q2[1] - 1
        return (x,y)

for l in s:
    dir, n = l.rstrip().split(' ')
    n = int(n)
    for i in range(n):
        p1 = ps[0]
        if dir == 'U':
            p1 = (p1[0], p1[1] + 1)
        elif dir == 'D':
            p1 = (p1[0], p1[1] - 1)
        elif dir == 'R':
            p1 = (p1[0] + 1, p1[1])
        else:
            p1 = (p1[0] - 1, p1[1])
        ps[0] = p1
        for j in range(1, len(ps)):
            ps[j] = update(ps[j-1], ps[j])
        pos.add(ps[-1])
print(len(pos))
