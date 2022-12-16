s = open('input', 'r').read().rstrip()
s = s.split('\n')
curr = 1
cycles = 0
res = ''
for i in range(len(s)):
    print(curr)
    l = s[i]
    l = l.strip()
    if abs(cycles % 40 - curr) <= 1:
        res += '#'
    else:
        res += '.'

    if l == 'noop':
        cycles += 1
        if cycles % 40 == 0:
            res += '\n'
    else:
        if cycles % 40 == 39:
            res += '\n'

        if abs((cycles + 1) % 40 - curr) <= 1:
            res += '#'
        else:
            res += '.'

        inst, n = l.split(' ')
        n = int(n)
        cycles += 2
        if cycles % 40 == 0:
            res += '\n'
        curr += n
print(res)
