from tqdm import tqdm
s = open('input', 'r').read().rstrip()
s = s.split('\n\n')
LEN = 8
items = [[] for _ in range(LEN)]

def op(i, v):
    if i == 0:
        return v * 5
    elif i == 1:
        return v + 7
    elif i == 2:
        return v + 5
    elif i == 3:
        return v + 8
    elif i == 4:
        return v + 4
    elif i == 5:
        return v * 2
    elif i == 6:
        return v * v
    elif i == 7:
        return v + 6

def op2(i, v):
    if i == 0:
        return v * 19
    elif i == 1:
        return v + 6
    elif i == 2:
        return v * v
    elif i == 3:
        return v + 3

throws = []
tests = []
prod = 1

for i in range(len(s)):
    m = s[i]
    m = m.split('\n')
    vals = m[1].split(': ')[1].split(', ')
    vals = list(map(int, vals))
    items[i] = vals
    test = m[3].split('by ')[1]
    t1 = m[4].split('monkey ')[1]
    t2 = m[5].split('monkey ')[1]
    tests.append(int(test))
    throws.append((int(t1), int(t2)))

for t in tests:
    prod *= t

inspects = [0 for _ in range(LEN)]
print(throws)
print(tests)
for r in tqdm(range(10000)):
    print(r)
    for m in range(LEN):
        for item in items[m]:
            inspects[m] += 1
            item = op(m, item)
            #item //= 3
            item %= prod
            if item % tests[m] == 0:
                items[throws[m][0]].append(item)
            else:
                items[throws[m][1]].append(item)
        items[m] = []

m1 = max(inspects)
inspects.remove(m1)
m2 = max(inspects)
print(m1 * m2)

