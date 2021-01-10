inp = open('input').read().split('\n\n')
inp = list(map(lambda x: x.split(), inp))
cnt = 0
for s in inp:
    res = set([])
    gg = 0
    for l in s:
        if gg == 0:
            res= set(l.rstrip())
            gg = 1
        else:
            res = res.intersection(set(l.rstrip()))
    cnt += len(res)
print(cnt)
