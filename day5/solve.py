dat = open('input', 'r').read().rstrip().split('\n')

def get_id(s):
    row = s[:7]
    lo = 0
    hi = 128
    for c in row:
        if c == 'F':
            hi = (lo + hi) // 2
        elif c == 'B':
            lo = (lo + hi) // 2
        else:
            assert(0)
    assert(hi - lo == 1)
    res = lo
    col = s[7:]
    lo = 0
    hi = 8
    for c in col:
        if c == 'L':
            hi = (lo + hi) // 2
        else:
            lo = (lo + hi) // 2
    assert(hi - lo == 1)
    res = res * 8 + lo
    return res

arr = []
for s in dat:
    arr.append(get_id(s))
arr = sorted(arr)
gg = range(70, 939)
for i in gg:
    if i not in arr:
        print(i)
        print()
print(arr[0])
print(max(arr))


