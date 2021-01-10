dat = open('input', 'r').read().rstrip().split('\n')
class Node:
    def __init__(self, nbs):
        self.nbs = nbs
cnt = 0
m = {}
for d in dat:
    d = d.split('bag')[:-1]
    t = d[0].rstrip()
    m[t] = cnt
    cnt += 1

nodes = []
for d in dat:
    d = d.replace("contain", ',').replace('.', '')
    d = d.split('bag')[:-1]
    t = d[0].rstrip()
    ss = list(map(lambda x: x.split(',')[1].rstrip(), d[1:]))
    ss1 = list(map(lambda x: ' '.join(x.split(' ')[2:]), ss))
    if ss1[0] == 'other':
        nums = []
    else:
        nums = list(map(lambda x: int(x.split(' ')[1]), ss))
    print(ss1, nums)
    gg = []
    for i in range(len(ss1)):
        s = ss1[i]
        if s == 'other':
            break
        gg.append((m[s], nums[i])) 
    nodes.append(gg)

s = m['shiny gold']
def solve(n):
    if nodes[n] == []:
        return 1
    else:
        res = 1
        for sub,num in nodes[n]:
            res += solve(sub) * num
        return res
print(solve(s))
'''
knowns = set([s])
prev_res = 0
curr_res = -1
while curr_res != prev_res:
    new_boy = set([])
    for k in knowns:
        new_boy = new_boy.union(set(nodes[k]))
    knowns = knowns.union(new_boy)
    prev_res = curr_res
    curr_res = len(knowns)
print(curr_res)



        
'''
