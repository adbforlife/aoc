with open("input", "r") as f:
    lines = f.readlines()

lines = list(map(int, lines))
for l1 in lines:
    for l2 in lines:
        for l3 in lines:
            if l1 + l2 + l3 == 2020:
                print(l1, l2, l3, l1 * l2 * l3)

