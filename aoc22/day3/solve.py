s = open('input', 'r').read().rstrip()
s = s.split('\n')
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = 0
for i in range(len(s)//3):
    l1 = s[i*3]
    l2 = s[i*3+1]
    l3 = s[i*3+2]
    for c in l1:
        if c in l2 and c in l3:
            res += alph.index(c) + 1
            break
print(res)
