from sys import stdin
input = stdin.readline

def check_available(y,x):
    global n, m, distance, maze
    if 0 > x or x >= m or 0 > y or y >= n:
        return False    
    elif distance[y][x] != -1:
        return False
    elif maze[y][x] == 0:
        return False
    else:
        return True

n,m = map(int,input().split())
distance = [ [-1 for _ in range(m)] for _ in range(n)]
maze = [[]for _ in range(n)]
for i in range(n):
    for x in input().rstrip():
        maze[i].append(int(x))

queue = [(0,0)]
distance[0][0] = 1

while queue:
    y, x = queue.pop(0)
    if check_available(y,x+1):
        queue.append((y,x+1))
        distance[y][x+1] = distance[y][x] + 1
    if check_available(y,x-1):
        queue.append((y,x-1))
        distance[y][x-1] = distance[y][x] + 1
    if check_available(y+1,x):
        queue.append((y+1,x))
        distance[y+1][x] = distance[y][x] + 1
    if check_available(y-1,x):
        queue.append((y-1,x))
        distance[y-1][x] = distance[y][x] + 1

print(distance[n-1][m-1])
