from sys import stdin

input = stdin.readline


def sti(n, m, board):
    max_sum = 0
    # 가로
    for i in range(n):
        for j in range(m - 3):
            c_sum = sum(board[i][j : j + 4])
            if max_sum < c_sum:
                max_sum = c_sum
    # 세로
    for i in range(n - 3):
        for j in range(m):
            c_sum = sum(board[a][j] for a in range(i, i + 4))
            if max_sum < c_sum:
                max_sum = c_sum
    return max_sum


def squ(n, m, board):
    max_sum = 0
    # 네모
    for i in range(n - 1):
        for j in range(m - 1):
            c_sum = sum(sum(board[a][j : j + 2]) for a in range(i, i + 2))
            if max_sum < c_sum:
                max_sum = c_sum
    return max_sum


def l(n, m, board):
    max_sum = 0
    # L
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[a][j] for a in range(i, i + 3)) + board[i + 2][j + 1]
            if max_sum < c_sum:
                max_sum = c_sum
    # 7
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[a][j + 1] for a in range(i, i + 3)) + board[i][j]
            if max_sum < c_sum:
                max_sum = c_sum
    # L 좌우대칭
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[a][j + 1] for a in range(i, i + 3)) + board[i + 2][j]
            if max_sum < c_sum:
                max_sum = c_sum
    # 7 좌우대칭
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[a][j] for a in range(i, i + 3)) + board[i][j + 1]
            if max_sum < c_sum:
                max_sum = c_sum
    # 가로로 긴 버전들
    # L
    for i in range(n - 1):
        for j in range(m - 2):
            c_sum = sum(board[i + 1][j : j + 3]) + board[i][j]
            if max_sum < c_sum:
                max_sum = c_sum
    # 7
    for i in range(n - 1):
        for j in range(m - 2):
            c_sum = sum(board[i][j : j + 3]) + board[i + 1][j + 2]
            if max_sum < c_sum:
                max_sum = c_sum
    # L대칭
    for i in range(n - 1):
        for j in range(m - 2):
            c_sum = sum(board[i + 1][j : j + 3]) + board[i][j + 2]
            if max_sum < c_sum:
                max_sum = c_sum
    # 7대칭
    for i in range(n - 1):
        for j in range(m - 2):
            c_sum = sum(board[i][j : j + 3]) + board[i + 1][j]
            if max_sum < c_sum:
                max_sum = c_sum
    return max_sum


def s(n, m, board):
    max_sum = 0
    # s
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[i + 1][j : j + 2]) + board[i][j] + board[i + 2][j + 1]
            if max_sum < c_sum:
                max_sum = c_sum
    # s대칭
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[i + 1][j : j + 2]) + board[i][j + 1] + board[i + 2][j]
            if max_sum < c_sum:
                max_sum = c_sum
    # z
    for i in range(n - 1):
        for j in range(m - 2):
            c_sum = (
                sum(board[a][j + 1] for a in range(i, i + 2))
                + board[i][j]
                + board[i + 1][j + 2]
            )
            if max_sum < c_sum:
                max_sum = c_sum
    # z대칭
    for i in range(n - 1):
        for j in range(m - 2):
            c_sum = (
                sum(board[a][j + 1] for a in range(i, i + 2))
                + board[i][j + 2]
                + board[i + 1][j]
            )
            if max_sum < c_sum:
                max_sum = c_sum
    return max_sum


def t(n, m, board):
    max_sum = 0
    # t
    for i in range(n - 1):
        for j in range(m - 2):
            c_sum = sum(board[i][j : j + 3]) + board[i + 1][j + 1]
            if max_sum < c_sum:
                max_sum = c_sum
    # ㅗ
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[i + 1][j : j + 3]) + board[i][j + 1]
            if max_sum < c_sum:
                max_sum = c_sum
    # ㅓ
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[a][j + 1] for a in range(i, i + 3)) + board[i + 1][j]
            if max_sum < c_sum:
                max_sum = c_sum
    # ㅏ
    for i in range(n - 2):
        for j in range(m - 1):
            c_sum = sum(board[a][j] for a in range(i, i + 3)) + board[i + 1][j + 1]
            if max_sum < c_sum:
                max_sum = c_sum
    return max_sum


def tetromino(n, m, board):
    return max(
        sti(n, m, board),
        squ(n, m, board),
        l(n, m, board),
        s(n, m, board),
        t(n, m, board),
    )


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(tetromino(n, m, board))
