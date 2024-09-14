from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

m = [[0 if i == "0" else 1 for i in input().rstrip()] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

danzi = []
for i in range(n):
    for j in range(n):
        if m[i][j] and not visited[i][j]:
            queue = deque()
            visited[i][j] = 1
            queue.append([i, j])
            cur_danzi_sum = 1
            while queue:
                x, y = queue.popleft()
                if x > 0 and not visited[x - 1][y] and m[x - 1][y]:
                    visited[x - 1][y] = 1
                    queue.append([x - 1, y])
                    cur_danzi_sum += 1
                if x < n - 1 and not visited[x + 1][y] and m[x + 1][y]:
                    visited[x + 1][y] = 1
                    queue.append([x + 1, y])
                    cur_danzi_sum += 1
                if y > 0 and not visited[x][y - 1] and m[x][y - 1]:
                    visited[x][y - 1] = 1
                    queue.append([x, y - 1])
                    cur_danzi_sum += 1
                if y < n - 1 and not visited[x][y + 1] and m[x][y + 1]:
                    visited[x][y + 1] = 1
                    queue.append([x, y + 1])
                    cur_danzi_sum += 1
            danzi.append(cur_danzi_sum)

print(len(danzi))
danzi.sort()
print(*danzi, sep="\n")
