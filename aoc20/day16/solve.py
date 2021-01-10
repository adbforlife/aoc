dat = open('input', 'r').read().rstrip().split('\n\n')
ranges = set()
rgs = []
for r in dat[0].split('\n'):
    r = r.split(': ')[1].split(' or ')
    r1 = r[0].split('-')
    r1 = list(map(int, r1))
    r2 = r[1].split('-')
    r2 = list(map(int, r2))
    print(r1, r2)
    ranges.add((r1[0], r1[1]))
    ranges.add((r2[0], r2[1]))
    rgs.append(r1 + r2)

rs = []
acc = 0
for r in dat[2].split('\n')[1:]:
    nums = r.split(',')
    nums = list(map(int, nums))
    bad = False
    for n in nums:
        ok = False
        for ra in ranges:
            if n >= ra[0] and n <= ra[1]:
                ok = True
        if not ok:
            acc += n
            bad = True
    if not bad:
        rs.append(nums)

mine = dat[1].split('\n')[1].split(',')
mine = list(map(int, mine))

print(len(rs))
res = 1
okss = []
for i in range(len(rgs)):
    oks = []
    for j in range(len(rs[0])):
        ok = True
        for r in rs:
            ok &= r[j] >= rgs[i][0] and r[j] <= rgs[i][1] or r[j] >= rgs[i][2] and r[j] <= rgs[i][3]
        if ok:
            oks.append(j)
    okss.append(oks)
    print(oks)
for _ in range(10):
    for i in range(len(okss)):
        if len(okss[i]) == 1:
            for j in range(len(okss)):
                if i != j:
                    try:
                        okss[j].remove(okss[i][0])
                    except:
                        pass
print(okss)
for i in range(6):
    res *= mine[okss[i][0]]
print(res)


