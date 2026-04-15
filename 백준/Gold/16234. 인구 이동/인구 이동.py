from sys import stdin

input = stdin.readline

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)


def move(i, j, visited):
    sum_population = 0
    queue = [(i, j)]
    visited[i][j] = True
    for i, j in queue:
        sum_population += board[i][j]
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if (
                0 <= ni < n
                and 0 <= nj < n
                and not visited[ni][nj]
                and l <= abs(board[i][j] - board[ni][nj]) <= r
            ):
                queue.append((ni, nj))
                visited[ni][nj] = True
    moved_population = sum_population // len(queue)
    for i, j in queue:
        board[i][j] = moved_population
    if len(queue) == 1:
        return False
    else:
        return True


n, l, r = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
count = 0

while True:
    moved = False
    visited = [[False] * n for _ in range(n)]
    for i, row in enumerate(board):
        for j, p in enumerate(row):
            if not visited[i][j]:
                moved = moved | move(i, j, visited)
    if not moved:
        break
    count += 1

print(count)
