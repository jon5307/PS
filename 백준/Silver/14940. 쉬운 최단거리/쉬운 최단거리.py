from collections import deque

# 입력받기
n, m = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]

# 변수 지정
map_dist = [[-1 for _ in range(m)] for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        # 원래 못가는 곳
        if map_data[i][j] == 0:
            map_dist[i][j] = 0
        # 시작점
        elif map_data[i][j] == 2:
            map_dist[i][j] = 0
            queue.append((i, j))

queue.append((-1, -1))

cur_dis = 1

while True:
    x, y = queue.popleft()
    if x == -1 and y == -1:
        if len(queue) == 0:
            break
        cur_dis += 1
        queue.append((-1, -1))
    else:
        explore = []
        if x > 0:
            explore.append((x - 1, y))
        if x < n - 1:
            explore.append((x + 1, y))
        if y > 0:
            explore.append((x, y - 1))
        if y < m - 1:
            explore.append((x, y + 1))
        for i, j in explore:
            if map_dist[i][j] == -1:
                map_dist[i][j] = cur_dis
                queue.append((i, j))

for i in range(n):
    print(*map_dist[i], sep=" ")
