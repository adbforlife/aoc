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
