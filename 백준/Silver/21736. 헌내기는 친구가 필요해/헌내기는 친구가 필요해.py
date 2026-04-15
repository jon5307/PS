from collections import deque
from sys import stdin

n,m = map(int,input().split())
campus = []
visited = [[0 for _ in range(m)] for _ in range(n)]
friend_c = 0
for _ in range(n):
    campus.append(stdin.readline().rstrip())
    
    
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            dy_y = i
            dy_x = j
            break

queue = deque()

queue.append((dy_y,dy_x))
visited[dy_y][dy_x] = 1

while queue:
    i,j = queue.popleft()
    if j>0 and campus[i][j-1] != "X" and visited[i][j-1] == 0:
        queue.append((i,j-1))
        visited[i][j-1] = 1
        if campus[i][j-1] == "P":
            friend_c += 1
            
    if j<m-1 and campus[i][j+1] != "X" and visited[i][j+1] == 0:
        queue.append((i,j+1))
        visited[i][j+1] = 1
        if campus[i][j+1] == "P":
            friend_c += 1
            
    if i>0 and campus[i-1][j] != "X" and visited[i-1][j] == 0:
        queue.append((i-1,j))
        visited[i-1][j] = 1
        if campus[i-1][j] == "P":
            friend_c += 1
            
    if i<n-1 and campus[i+1][j] != "X" and visited[i+1][j] == 0:
        queue.append((i+1,j))
        visited[i+1][j] = 1
        if campus[i+1][j] == "P":
            friend_c += 1
        
if friend_c == 0:
    print("TT")
else:
    print(friend_c)
        