from sys import stdin

input = stdin.readline

dx = (0, 0, 1, -1)
dy = (-1, 1, 0, 0)

r, c = map(int, input().rstrip().split())
board = [input().rstrip() for _ in range(r)]

visited_alphabet = set()

visited_alphabet.add(board[0][0])


def dfs(i, j):
    max_count = 0
    for a in range(4):
        ni = i + dy[a]
        nj = j + dx[a]
        if ni >= 0 and ni < r and nj >= 0 and nj < c:
            if  board[ni][nj] not in visited_alphabet:
                visited_alphabet.add(board[ni][nj])
                max_count = max(dfs(ni, nj) + 1, max_count)
                visited_alphabet.remove(board[ni][nj])
    return max_count

print(dfs(0, 0) + 1)
