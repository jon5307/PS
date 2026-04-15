from sys import stdin
from collections import deque

input = stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n = int(input())

space = [list(map(int, input().rstrip().split())) for _ in range(n)]

shark_size = 2
eat_count = 0
time = 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_i, shark_j = i, j
            space[i][j] = 0
            break


def eat_fastest():
    global shark_i, shark_j, eat_count, shark_size, time, n
    queue = deque()
    queue.append((shark_i, shark_j))
    distance = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[shark_i][shark_j] = True
    new_i, new_j = -1, -1
    while queue:
        prio = n**2 + 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for a in range(4):
                ni, nj = i + dy[a], j + dx[a]
                if (
                    0 <= ni < n
                    and 0 <= nj < n
                    and space[ni][nj] <= shark_size
                    and not visited[ni][nj]
                ):
                    visited[ni][nj] = True
                    queue.append((ni, nj))
                    if 0 < space[ni][nj] < shark_size:
                        if ni * n + nj < prio:
                            prio = ni * n + nj
                            new_i, new_j = ni, nj
        distance += 1
        if prio != n**2 + 1:
            space[new_i][new_j] = 0
            shark_i, shark_j = new_i, new_j
            eat_count += 1
            if eat_count == shark_size:
                shark_size += 1
                eat_count = 0
            return distance
    return -1


while True:
    move_distance = eat_fastest()
    if move_distance == -1:
        print(time)
        break
    time += move_distance
