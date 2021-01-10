from copy import *
dat = open('input', 'r').read().rstrip().split('\n')
fs = []
al_set = set()
ing_set = set()
for r in dat:
    ings, als = r.split(' (contains ')
    als = als[:-1].split(', ')
    ings = ings.split(' ')
    fs.append((ings, als))
    for al in als:
        al_set.add(al)
    for ing in ings:
        ing_set.add(ing)

als = list(al_set)
ings = list(ing_set)
possibles = []
for al in als:
    res_set = copy(ing_set)
    for f in fs:
        if al in f[1]:
            res_set = res_set.intersection(set(f[0]))

    possibles.append(res_set)
for p in possibles:
    print(len(p), p)


def red(pos):
    new_pos = []
    taken = ''
    for i in range(len(pos)):
        p = pos[i]
        if len(p) == 1:
            for gg in p:
                taken = gg
            for j in range(len(pos)):
                p = pos[j]
                if len(p) != 1 and taken in p:
                    p.remove(taken)

for _ in range(10):
    red(possibles)
for p in possibles:
    print(p)

takens = set()
for p in possibles:
    for gg in p:
        takens.add(gg)

cnt = 0
for f in fs:
    for ing in f[0]:
        cnt += ing not in takens
print(cnt)


for i in range(len(als)):
    print(als[i], possibles[i])




print(len(al_set))
print(len(ing_set))
print(len(dat))


