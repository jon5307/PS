from sys import stdin
from collections import deque

input = stdin.readline
di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

n, m = map(int, input().rstrip().split())

map_grid = [input().rstrip() for _ in range(n)]


def find_farthest(i, j):
    distance = -1
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if (
                    0 <= ni < n
                    and 0 <= nj < m
                    and not visited[ni][nj]
                    and map_grid[ni][nj] == "L"
                ):
                    visited[ni][nj] = True
                    queue.append((ni, nj))
        distance += 1
    return distance


farthest = -1
for i in range(n):
    for j in range(m):
        if map_grid[i][j] == "L":
            farthest = max(farthest, find_farthest(i, j))

print(farthest)
