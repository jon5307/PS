from sys import stdin
input = stdin.readline
from collections import deque


m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append(i)
                queue.append(j)
                queue.append(k)
queue.append(-1)
days = 0

while queue:
    z = queue.popleft()
    if z == -1:
        if len(queue) == 0:
            break
        days += 1
        queue.append(-1)
    else:
        y = queue.popleft()
        x = queue.popleft()
        if 0 <= x-1 and x-1 < m and 0 <= y and y < n and 0 <= z and z < h and tomato[z][y][x-1] == 0:
            tomato[z][y][x-1] = 1
            queue.append(z)
            queue.append(y)
            queue.append(x-1)
        if 0 <= x+1 and x+1 < m and 0 <= y and y < n and 0 <= z and z < h and tomato[z][y][x+1] == 0:
            tomato[z][y][x+1] = 1
            queue.append(z)
            queue.append(y)
            queue.append(x+1)
        if 0 <= x and x < m and 0 <= y-1 and y-1 < n and 0 <= z and z < h and tomato[z][y-1][x] == 0:
            tomato[z][y-1][x] = 1
            queue.append(z)
            queue.append(y-1)
            queue.append(x)
        if 0 <= x and x < m and 0 <= y+1 and y+1 < n and 0 <= z and z < h and tomato[z][y+1][x] == 0:
            tomato[z][y+1][x] = 1
            queue.append(z)
            queue.append(y+1)
            queue.append(x)
        if 0 <= x and x < m and 0 <= y and y < n and 0 <= z-1 and z-1 < h and tomato[z-1][y][x] == 0:
            tomato[z-1][y][x] = 1
            queue.append(z-1)
            queue.append(y)
            queue.append(x)
        if 0 <= x and x < m and 0 <= y and y < n and 0 <= z+1 and z+1 < h and tomato[z+1][y][x] == 0:
            tomato[z+1][y][x] = 1
            queue.append(z+1)
            queue.append(y)
            queue.append(x)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
print(days)
