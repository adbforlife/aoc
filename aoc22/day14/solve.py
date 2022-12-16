s = open('input', 'r').read().rstrip()
s = s.split('\n')
grid = [[0 for _ in range(1000)] for _ in range(200)]
highest_y = 0
for i in range(len(s)):
    l = s[i].rstrip()
    l = l.split(' -> ')
    for j in range(len(l)-1):
        a1,b1 = l[j].split(',')
        a2,b2 = l[j+1].split(',')
        a1 = int(a1)
        b1 = int(b1)
        a2 = int(a2)
        b2 = int(b2)
        highest_y = max(highest_y, b1)
        highest_y = max(highest_y, b2)
        if a1 == a2:
            for c in range(min(b1, b2), max(b1, b2) + 1):
                grid[c][a1] = 1
        else:
            assert(b1 == b2)
            for c in range(min(a1, a2), max(a1, a2) + 1):
                grid[b1][c] = 1

for i in range(len(grid[0])):
    grid[highest_y + 2][i] = 1

start = [0, 500]
res = 0
while True:
    a,b = start
    if grid[a][b] == 1:
        break
    done = False
    while True:
        if a+1 >= len(grid):
            done = True
            break
        elif grid[a+1][b] == 0:
            a,b = a+1,b
        elif grid[a+1][b-1] == 0:
            a,b = a+1,b-1
        elif grid[a+1][b+1] == 0:
            a,b = a+1,b+1
        else:
            grid[a][b] = 1
            break
    if done:
        break
    res += 1
print(res)
