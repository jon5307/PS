from sys import stdin
input = stdin.readline
from collections import deque


m,n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i,j))
queue.append((-1,-1))
days = 0

while queue:
    y,x = queue.popleft()
    if y == -1:
        if len(queue) == 0:
            break
        days += 1
        queue.append((-1,-1))
    else:
        if 0 <= x-1 and x-1 < m and 0 <= y and y < n and tomato[y][x-1] == 0:
            tomato[y][x-1] = 1
            queue.append((y,x-1))
        if 0 <= x+1 and x+1 < m and 0 <= y and y < n and tomato[y][x+1] == 0:
            tomato[y][x+1] = 1
            queue.append((y,x+1))
        if 0 <= x and x < m and 0 <= y-1 and y-1 < n and tomato[y-1][x] == 0:
            tomato[y-1][x] = 1
            queue.append((y-1,x))
        if 0 <= x and x < m and 0 <= y+1 and y+1 < n and tomato[y+1][x] == 0:
            tomato[y+1][x] = 1
            queue.append((y+1,x))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
print(days)
