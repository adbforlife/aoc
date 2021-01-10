dat = open('input', 'r').read().rstrip().split('\n')
board = [[] for _ in range(len(dat))]
for i in range(len(dat)):
    r = dat[i]
    for c in r:
        if c == '.':
            board[i].append(0)
        elif c == 'L':
            board[i].append(1)
        else:
            board[i].append(2)
print(board)



def get_occ(board, i, j):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return 0
    if board[i][j] == 2:
        return 1
    if board[i][j] == 1:
        return 0
    return None

def get_num_occ(board, i, j):
    acc = 0

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii-1,jj-1
        res = get_occ(board,ii,jj)
    acc += res

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii-1,jj
        res = get_occ(board,ii,jj)
    acc += res

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii-1,jj+1
        res = get_occ(board,ii,jj)
    acc += res

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii,jj-1
        res = get_occ(board,ii,jj)
    acc += res

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii,jj+1
        res = get_occ(board,ii,jj)
    acc += res

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii+1,jj-1
        res = get_occ(board,ii,jj)
    acc += res

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii+1,jj
        res = get_occ(board,ii,jj)
    acc += res

    res = None
    ii,jj = i,j
    while res is None:
        ii,jj = ii+1,jj+1
        res = get_occ(board,ii,jj)
    acc += res
    return acc

def round():
    swaps = []
    for i in range(len(dat)):
        for j in range(len(dat[0])):
            num = get_num_occ(board, i, j)
            if board[i][j] == 1:
                if num == 0:
                    swaps.append((i,j))
            if board[i][j] == 2:
                if num >= 5:
                    swaps.append((i,j))
    if len(swaps) == 0:
        res = 0
        for i in range(len(dat)):
            for j in range(len(dat[0])):
                if board[i][j] == 2:
                    res += 1
        print(res)
        exit(0)
    print(len(swaps))
    for i,j in swaps:
        if board[i][j] == 1:
            board[i][j] = 2
        else:
            board[i][j] = 1
for i in range(200):
    print(i)
    round()
