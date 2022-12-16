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
v_names = []
good_v_names = []

cache = {}
def num_to_names(n):
    og_n = n
    if n in cache:
        return cache[n]

    res = []
    for i in range(len(good_v_names)):
        b = n % 2
        if b:
            res.append(good_v_names[i])
        n //= 2
    cache[og_n] = res
    return res

def names_to_num(names):
    res = 0
    for i in range(len(good_v_names)):
        name = good_v_names[i]
        if name in names:
            res += 2**i
    return res

valves = {}
res = 0
for i in range(len(s)):
    l = s[i]
    v = l[6:8]
    l = l.split('=')[1]
    f = int(l.split(';')[0])
    l = l.split('to valve')[1]
    if l[0] == 's':
        l = l[1:]
    l = l[1:]
    leads = l.rstrip().split(', ')
    leads = {lead : 1 for lead in leads}
    valves[v] = (f, leads)
    v_names.append(v)
    if f > 0:
        good_v_names.append(v)

print(res)
print(valves)

'''
def remove_w(w):
    global valves
    assert(valves[w][0] == 0)
    w_targets = valves[w][1]
    for v in valves:
        f, targets = valves[v]
        if w in targets:
            dist = targets[w]
            targets.pop(w)
            for u in w_targets:
                if u == w:
                    print(w, w_targets)
                assert(u != w)
                if v != u and u not in targets:
                    targets[u] = dist + w_targets[u]
    if w != 'AA':
        valves.pop(w)

print()
for w in v_names:
    if w not in good_v_names:
        remove_w(w)
print(valves)
print(len(valves))
'''

# dp[i][j][k]: time i, starting at j, having k
dp = [[[0 for _ in range(2**len(good_v_names))] for _ in range(len(s) * len(s))] for _ in range(26)]

def get_trajs(time, start):
    res = [[start]]
    if time <= 1:
        return res
    f, targets = valves[start]
    for target in targets:
        target_time = targets[target]
        target_trajs = get_trajs(time - target_time, target)
        res += list(map(lambda traj : [start] + traj, target_trajs))
    return res

for i in tqdm(range(26)):
    for j in range(len(valves) * len(valves)):
        j1 = j % len(valves)
        j2 = j // len(valves)
        name1 = v_names[j1]
        name2 = v_names[j2]
        val1 = valves[name1][0]
        val2 = valves[name2][0]
        targets1 = valves[name1][1]
        targets2 = valves[name2][1]
        idx1 = v_names.index(name1)
        idx2 = v_names.index(name2)
        for k in range(2**len(good_v_names)):
            open_names = num_to_names(k)
            for v in open_names:
                dp[i][j][k] += valves[v][0]
            if i == 0:
                continue

            best = 0
            for target1 in targets1:
                for target2 in targets2:
                    target_idx1 = v_names.index(target1)
                    target_idx2 = v_names.index(target2)
                    target_idx = target_idx1 + len(valves) * target_idx2
                    best = max(best, dp[i-1][target_idx][k])

                    if not ( name2 in open_names or val2 == 0):
                        # human move
                        k1 = names_to_num(open_names + [name2])
                        best = max(best, dp[i-1][target_idx1 + len(valves) * idx2][k1])
                    if not ( name1 in open_names or val1 == 0):
                        # elephant move
                        k2 = names_to_num(open_names + [name1])
                        best = max(best, dp[i-1][idx1 + len(valves) * target_idx2][k2])
                    if (not ( name2 in open_names or val2 == 0)) and (not ( name1 in open_names or val1 == 0)):
                        k3 = names_to_num(open_names + [name1, name2])
                        best = max(best, dp[i-1][idx1 + len(valves) * idx2][k3])

            dp[i][j][k] += best
print(dp[25][3][0])

