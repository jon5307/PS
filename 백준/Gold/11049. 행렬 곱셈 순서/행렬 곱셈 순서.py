from sys import stdin

input = stdin.readline
MAX = 2**31 - 1

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

dp = [[MAX] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0
for i in range(n - 1):
    dp[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]

for i in range(2, n):
    for s in range(n - i):
        e = s + i
        for m in range(s, e):
            dp[s][e] = min(
                dp[s][e],
                dp[s][m] + dp[m + 1][e] + matrix[s][0] * matrix[m][1] * matrix[e][1],
            )

print(dp[0][n - 1])
