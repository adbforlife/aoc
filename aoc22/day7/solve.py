s = open('input', 'r').read().rstrip()
s = s.split('\n')

class Node:
    def __init__(self, ls, val, is_dir, name, parent):
        self.is_dir = is_dir
        self.ls = ls
        self.val = val
        self.name = name
        self.parent = parent

res = 0
print(len(s))
root = Node([], 0, True, "/", None)
curr = root
for i in range(1, len(s)):
    l = s[i]
    if l[:4] == "$ ls":
        assert(len(curr.ls) == 0)
        j = i+1
        while j < len(s) and s[j][0] != "$":
            num, name = s[j].split(' ')[0], s[j].split(' ')[1]
            if num != 'dir':
                curr.ls.append(Node([], int(num), False, name, curr))
            else:
                curr.ls.append(Node([], 0, True, name, curr))
            j += 1
    elif l[:7] == "$ cd ..":
        curr = curr.parent
    elif l[:5] == "$ cd ":
        name = l.split(' ')[2]
        changed = False
        for n in curr.ls:
            print(name, n.name)
            if n.name == name:
                assert(n.is_dir)
                curr = n
                changed = True
                break
        assert(changed)

def explore(n):
    global res
    val = 0
    assert(len(n.ls) > 0)
    for m in n.ls:
        if m.is_dir:
            explore(m)
            val += m.val
        else:
            val += m.val
    n.val = val
    if n.val <= 100000:
        res += n.val


explore(root)
free = 70000000 - root.val
need = 30000000 - free
best = root.val
print(need)
def find(n):
    global best
    if n.val >= need:
        best = min(n.val, best)
    for m in n.ls:
        find(m)
find(root)
print(best)
