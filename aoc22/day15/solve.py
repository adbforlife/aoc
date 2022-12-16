from tqdm import tqdm
fake = False
if fake:
    inp = 'input2'
    y = 10
else:
    inp = 'input'
    y = 2000000

s = open(inp, 'r').read().rstrip()
s = s.split('\n')
sensors = []
beacons = []
for i in range(len(s)):
    l = s[i]
    a,b = l.split('x=')[1:]
    x1,y1 = a.split(', y=')
    x1 = int(x1)
    y1 = int(y1.split(':')[0])
    x2,y2 = b.split(', y=')
    x2 = int(x2)
    y2 = int(y2)
    sensors.append((x1,y1))
    beacons.append((x2,y2))


ranges = []
def combine(ranges, r):
    a,b = r
    for i in range(len(ranges)):
        c,d = ranges[i]
        if d < a:
            continue
        elif b < c:
            ranges.insert(i, (a,b))
            return
        else:
            ranges.pop(i)
            combine(ranges, (min(a,c), max(b,d)))
            return
    ranges.append((a,b))


def find_ranges(y):
    ranges = []
    for i in range(len(sensors)):
        x1,y1 = sensors[i]
        x2,y2 = beacons[i]
        dist = abs(x1 - x2) + abs(y1 - y2)
        dy = abs(y1 - y)
        if dy > dist:
            continue
        else:
            a = x1 - (dist - dy)
            b = x1 + (dist - dy)
            combine(ranges, (a,b))
    return ranges


for y in tqdm(range(2500000,4000000)):
    ranges = find_ranges(y)
    if len(ranges) >= 2:
        print(ranges)
        print(y)

