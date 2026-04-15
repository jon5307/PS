from sys import stdin
from collections import deque

input = stdin.readline
di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

m, n = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(m)]

dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]
dp[0][0] = [1, 0, 0, 0]
queue = deque()
queue.append((0, 0))

while queue:
    y, x = queue.popleft()
    for d in range(4):
        ny, nx = y + di[d], x + dj[d]
        if 0 <= ny < m and 0 <= nx < n:
            if board[y][x] > board[ny][nx]:
                if dp[ny][nx][d] != sum(dp[y][x]):
                    queue.append((ny, nx))
                dp[ny][nx][d] = sum(dp[y][x])

print(sum(dp[m - 1][n - 1]))
