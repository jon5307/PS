from sys import stdin

input = stdin.readline

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

r, c, t = map(int, input().rstrip().split())
room = [list(map(int, input().rstrip().split())) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            ap_r1 = i - 1
            ap_r2 = i
            break

for _ in range(t):
    # 확산
    diffusion = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                diffusion_amount = room[i][j] // 5
                for d in range(4):
                    ni = i + dy[d]
                    nj = j + dx[d]
                    if ni >= 0 and r > ni and nj >= 0 and c > nj and room[ni][nj] != -1:
                        diffusion[ni][nj] += diffusion_amount
                        room[i][j] -= diffusion_amount
    for i in range(r):
        for j in range(c):
            room[i][j] += diffusion[i][j]
    # 공기청정기
    # 위쪽
    j = 0
    for i in range(ap_r1 - 1, 0, -1):
        room[i][j] = room[i - 1][j]
    i = 0
    for j in range(c - 1):
        room[i][j] = room[i][j + 1]
    j = c - 1
    for i in range(ap_r1):
        room[i][j] = room[i + 1][j]
    i = ap_r1
    for j in range(c - 1, 1, -1):
        room[i][j] = room[i][j - 1]
    room[ap_r1][1] = 0
    # 아래쪽
    j = 0
    for i in range(ap_r2 + 1, r - 1):
        room[i][j] = room[i + 1][j]
    i = r - 1
    for j in range(c - 1):
        room[i][j] = room[i][j + 1]
    j = c - 1
    for i in range(r - 1, ap_r2, -1):
        room[i][j] = room[i - 1][j]
    i = ap_r2
    for j in range(c - 1, 1, -1):
        room[i][j] = room[i][j - 1]
    room[ap_r2][1] = 0

sum = 0
for row in room:
    for i in row:
        if i > 0:
            sum += i
print(sum)
