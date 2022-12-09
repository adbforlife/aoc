s = open('input', 'r').read().rstrip()
cs = set([])
i = 0
for i in range(len(s)):
    cs = set([])
    for j in range(14):
        cs.add(s[i+j])
    if len(cs) == 14:
        print(i + 14)
        exit(0)
