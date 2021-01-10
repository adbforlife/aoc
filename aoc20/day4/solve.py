dat = open('input', 'r').read().rstrip().split('\n\n')
dat = list(map(lambda x: x.replace('\n', ' ').split(' '), dat))
cnt = 0

def prefix(s):
    return s.split(':')[0]
def suffix(s):
    return s.split(':')[1].rstrip()

wanted = {'byr', 'iyr', 'hgt', 'eyr', 'ecl', 'pid', 'cid', 'hcl'}
for pas in dat:
    maps = {}
    for w in wanted:
        maps[w] = '0'
    for item in pas:
        maps[prefix(item)] = suffix(item)
    if len(maps['byr']) != 4:
        continue
    if int(maps['byr']) < 1920 or int(maps['byr']) > 2002:
        continue
    if int(maps['iyr']) < 2010 or int(maps['iyr']) > 2020:
        continue
    if int(maps['eyr']) < 2020 or int(maps['eyr']) > 2030:
        continue
    
    hgt = maps['hgt']
    if hgt[-2:] == 'cm':
        if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
            continue
    elif hgt[-2:] == 'in':
        if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
            continue
    else:
        continue

    hcl = maps['hcl']
    if hcl[0] != "#":
        continue
    if len(hcl) != 7:
        continue
    bad = False
    for c in hcl[1:]:
        if c not in "0123456789abcdef":
            bad = True
    if bad:
        continue

    if maps['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue

    if len(maps['pid']) != 9:
        continue
    for c in maps['pid']:
        if c not in "0123456789":
            bad = True
    if bad:
        continue

    cnt += 1
print(cnt)
print(len(dat))

print(dat[:10])
