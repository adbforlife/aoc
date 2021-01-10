starts = [6,19,0,5,7,13,1]
m = {6:1, 19: 2, 0: 3, 5: 4, 7: 5, 13: 6, 1: 7}
for k in m:
    m[k] = (-1, m[k])
for i in range(8, 30000001):
    l = starts[-1]
    c,d = m[l]
    if c == -1:
        starts.append(0)
        e,f = m[0]
        m[0] = (f, len(starts))
    else:
        if d-c in m:
            starts.append(d-c)
            e,f = m[d-c]
            m[d-c] = (f, len(starts))
        else:
            starts.append(d-c)
            m[d-c] = (-1, len(starts))
    '''
    try:
        a = starts[:-1][::-1].index(l)
    except:
        a = -1
    if a == -1:
        n = 0
    else:
        n = a + 1

    starts.append(n)
    '''
    if i % 10000 == 0:
        print(i)
print(starts[-1])
