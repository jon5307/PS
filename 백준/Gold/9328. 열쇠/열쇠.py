from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**8)
input = stdin.readline

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)


def find(i, j):
    global building, key, visited, available
    docu_count = 0
    status = building[i][j]
    if status == "*" or visited[i][j]:
        return 0
    if ord("A") <= ord(status) <= ord("Z") and building[i][j].lower() not in key:
        available.append((i, j))
        return 0
    visited[i][j] = True
    if status == "$":
        docu_count += 1
    elif ord("a") <= ord(status) <= ord("z") and status not in key:
        key.append(status)
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if (
            0 <= ni < h
            and 0 <= nj < w
            and not visited[ni][nj]
            and building[ni][nj] != "*"
        ):
            docu_count += find(ni, nj)
    return docu_count


for _ in range(int(input())):
    h, w = map(int, input().rstrip().split())
    building = [input().rstrip() for _ in range(h)]
    key = []
    for k in input().rstrip():
        key.append(k)
    visited = [[False] * w for _ in range(h)]
    available = deque()
    docu_count = 0
    for i in range(h):
        docu_count += find(i, 0)
        docu_count += find(i, w - 1)
    for j in range(1, w - 1):
        docu_count += find(0, j)
        docu_count += find(h - 1, j)

    while available:
        cur_key = len(key)
        for _ in range(len(available)):
            i, j = available.popleft()
            docu_count += find(i, j)
        if len(key) == cur_key:
            break
    print(docu_count)
