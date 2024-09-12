from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

num = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        prefix[i][j] = num[i][j]
        if i > 0:
            prefix[i][j] += prefix[i - 1][j]
        if j > 0:
            prefix[i][j] += prefix[i][j - 1]
        if i > 0 and j > 0:
            prefix[i][j] -= prefix[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    p_sum = prefix[x2][y2]
    if not x1 == 0:
        p_sum -= prefix[x1 - 1][y2]
    if not y1 == 0:
        p_sum -= prefix[x2][y1 - 1]
    if x1 != 0 and y1 != 0:
        p_sum += prefix[x1 - 1][y1 - 1]
    print(p_sum)
