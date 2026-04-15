from sys import stdin

input = stdin.readline

a = input().rstrip()
b = input().rstrip()

dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
dp_before = [[None for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            dp_before[i][j] = (i - 1, j - 1)
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                dp[i][j] = dp[i][j - 1]
                dp_before[i][j] = (i, j - 1)
            else:
                dp[i][j] = dp[i - 1][j]
                dp_before[i][j] = (i - 1, j)
mi, mj = 0, 0
max_len = -1
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if max_len < dp[i][j]:
            mi, mj = i, j
            max_len = dp[i][j]

print(max_len)
route = []
while mi > 0 and mj > 0:
    if dp_before[mi][mj] == (mi - 1, mj - 1) and a[mi - 1] == b[mj - 1]:
        route.append(a[mi - 1])
    mi, mj = dp_before[mi][mj]

print(*route[::-1], sep="")
