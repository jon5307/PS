from sys import stdin
from copy import deepcopy

input = stdin.readline


def move(board, direction):
    # direction 0상 1우 2하 3좌
    new_board = deepcopy(board)
    combined = [[False for _ in range(n)] for _ in range(n)]
    if direction == 0:
        for j in range(n):
            for i in range(1, n):
                if new_board[i][j] == 0:
                    continue
                for ni in range(i - 1, -1, -1):
                    if new_board[ni][j] == 0:
                        new_board[ni][j] = new_board[ni + 1][j]
                        new_board[ni + 1][j] = 0
                    elif (
                        new_board[ni][j] == new_board[ni + 1][j] and not combined[ni][j]
                    ):
                        new_board[ni][j] *= 2
                        new_board[ni + 1][j] = 0
                        combined[ni][j] = True
                        break
                    else:
                        break
    elif direction == 1:
        for i in range(n):
            for j in range(n - 2, -1, -1):
                if new_board[i][j] == 0:
                    continue
                for nj in range(j + 1, n):
                    if new_board[i][nj] == 0:
                        new_board[i][nj] = new_board[i][nj - 1]
                        new_board[i][nj - 1] = 0
                    elif (
                        new_board[i][nj] == new_board[i][nj - 1] and not combined[i][nj]
                    ):
                        new_board[i][nj] *= 2
                        new_board[i][nj - 1] = 0
                        combined[i][nj] = True
                        break
                    else:
                        break
    elif direction == 2:
        for j in range(n):
            for i in range(n - 2, -1, -1):
                if new_board[i][j] == 0:
                    continue
                for ni in range(i + 1, n):
                    if new_board[ni][j] == 0:
                        new_board[ni][j] = new_board[ni - 1][j]
                        new_board[ni - 1][j] = 0
                    elif (
                        new_board[ni][j] == new_board[ni - 1][j] and not combined[ni][j]
                    ):
                        new_board[ni][j] *= 2
                        new_board[ni - 1][j] = 0
                        combined[ni][j] = True
                        break
                    else:
                        break
    elif direction == 3:
        for i in range(n):
            for j in range(1, n):
                if new_board[i][j] == 0:
                    continue
                for nj in range(j - 1, -1, -1):
                    if new_board[i][nj] == 0:
                        new_board[i][nj] = new_board[i][nj + 1]
                        new_board[i][nj + 1] = 0
                    elif (
                        new_board[i][nj] == new_board[i][nj + 1] and not combined[i][nj]
                    ):
                        new_board[i][nj] *= 2
                        new_board[i][nj + 1] = 0
                        combined[i][nj] = True
                        break
                    else:
                        break
    return new_board


def max_value(board):
    max_v = 0
    for col in board:
        for value in col:
            max_v = max(max_v, value)
    return max_v


def dfs(n, board):
    if n == 5:
        return max_value(board)
    else:
        max_v = 0
        for i in range(4):
            max_v = max(max_v, dfs(n + 1, move(board, i)))
        return max_v


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))

print(dfs(0, board))
