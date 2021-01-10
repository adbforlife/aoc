m = open("input", "r").readlines()
print(len(m))
m = list(map(lambda x: x.rstrip(), m))

res = 1
def solve1(a):
    cnt = 0
    for i in range(len(m)):
        pos = i * a % len(m[0])
        if m[i][pos] == "#":
            cnt += 1
    return cnt
res *= solve1(1)
res *= solve1(3)
res *= solve1(5)
res *= solve1(7)

def solve2():
    cnt = 0
    for i in range(0, len(m), 2):
        pos = i // 2 % len(m[0])
        if m[i][pos] == "#":
            cnt += 1
    return cnt
res *= solve2()
print(res)
