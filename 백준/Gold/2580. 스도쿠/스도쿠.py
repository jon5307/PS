from sys import stdin

input = stdin.readline


board = []
for _ in range(9):
    board.append(list(map(int, input().rstrip().split())))


def check(y, x, v):
    for i in range(9):
        if board[i][x] == v and i != y:
            return False
    for j in range(9):
        if board[y][j] == v and j != x:
            return False
    for i in range(3 * (y // 3), 3 * (y // 3) + 3):
        for j in range(3 * (x // 3), 3 * (x // 3) + 3):
            if board[i][j] == v and i != y and j != x:
                return False
    return True


def bt(y, x):
    if y >= 9:
        return True
    nx = (x + 1) % 9
    ny = y + (x + 1) // 9
    if board[y][x] != 0:
        return bt(ny, nx)
    for v in range(1, 10):
        if check(y, x, v):
            board[y][x] = v
            if bt(ny, nx):
                return True
            board[y][x] = 0
    return False


bt(0, 0)
for b in board:
    print(*b, sep=" ", end="\n")
