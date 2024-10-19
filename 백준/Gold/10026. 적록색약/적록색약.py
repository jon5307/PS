from sys import stdin
from collections import deque

input = stdin.readline


n = int(input())
pic = [input().rstrip() for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 적록색약X
groups_not_rg = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i, ver in enumerate(pic):
    for j, color in enumerate(ver):
        if not visited[i][j]:
            groups_not_rg += 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 > new_row or 0 > new_col or n <= new_row or n <= new_col:
                        continue
                    if not visited[new_row][new_col] and pic[new_row][new_col] == color:
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))

# 적록색약X
groups_rg = 0
visited = [[False for _ in range(n)] for _ in range(n)]
rg = ("R", "G")
for i, ver in enumerate(pic):
    for j, color in enumerate(ver):
        if not visited[i][j]:
            groups_rg += 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 > new_row or 0 > new_col or n <= new_row or n <= new_col:
                        continue
                    if not visited[new_row][new_col] and (
                        pic[new_row][new_col] in rg
                    ) == (color in rg):
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))

print(groups_not_rg, groups_rg)
