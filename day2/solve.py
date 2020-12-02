lines = open("input").readlines()
cnt = 0
for l in lines:
    ws = l.split(" ")
    lo = int(ws[0].split("-")[0])
    hi = int(ws[0].split("-")[1])
    c = ws[1][0:1]
    w = ws[2]
    part = 0
    if w[lo-1] == c:
        part += 1
    if w[hi-1] == c:
        part += 1
    if part == 1:
        cnt += 1
    '''
    if w.count(c) >= lo and w.count(c) <= hi:
        cnt += 1
    '''
print(cnt)
