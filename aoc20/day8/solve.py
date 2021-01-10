from copy import *
old_dat = open('input', 'r').read().rstrip().split('\n')
for i in range(len(old_dat)):
    dat = copy(old_dat)
    if dat[i].split()[0] == "nop":
        dat[i] = "jmp " + dat[i].split()[1]
    elif dat[i].split()[0] == "jmp":
        dat[i] = "nop " + dat[i].split()[1]
    else:
        continue
    e = set([])
    yeet = True
    res = 0
    pc = 0
    while True:
        if pc in e or pc > len(dat):
            yeet = False
            break
        if pc == len(dat):
            break
        instr = dat[pc].split(' ')
        e.add(pc)
        if instr[0] == "nop":
            pc += 1
        elif instr[0] == "acc":
            pc += 1
            res += int(instr[1])
        else:
            pc += int(instr[1])
    if yeet:
        print(res)
     

print(res)


