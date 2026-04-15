from sys import stdin
from collections import deque

input = stdin.readline

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

r, c = map(int, input().rstrip().split())

queue = deque()

miro = [list(input().rstrip()) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if miro[i][j] == "J":
            queue.appendleft((i, j))
        elif miro[i][j] == "F":
            queue.append((i, j))

t = 1
while queue:
    new_queue = deque()
    for _ in range(len(queue)):
        i, j = queue.popleft()
        if miro[i][j] == "F":
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if (
                    0 <= ni < r
                    and 0 <= nj < c
                    and (miro[ni][nj] == "." or miro[ni][nj] == "J")
                ):
                    miro[ni][nj] = "F"
                    new_queue.append((ni, nj))
        else:
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if ni < 0 or ni >= r or nj < 0 or nj >= c:
                    print(t)
                    exit()
                if miro[ni][nj] == ".":
                    miro[ni][nj] = "J"
                    new_queue.appendleft((ni, nj))
    t += 1
    queue = new_queue
print("IMPOSSIBLE")
