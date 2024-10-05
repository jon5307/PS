from sys import stdin

input = stdin.readline

# Constants for directions
HORIZONTAL = 0
DIAGONAL = 1
VERTICAL = 2

n = int(input())
home = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][HORIZONTAL] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j][HORIZONTAL]:
            if j + 1 < n and home[i][j + 1] == 0:
                dp[i][j + 1][HORIZONTAL] += dp[i][j][HORIZONTAL]
            if (
                i + 1 < n
                and j + 1 < n
                and home[i + 1][j] == 0
                and home[i][j + 1] == 0
                and home[i + 1][j + 1] == 0
            ):
                dp[i + 1][j + 1][DIAGONAL] += dp[i][j][HORIZONTAL]
        if dp[i][j][VERTICAL]:
            if i + 1 < n and home[i + 1][j] == 0:
                dp[i + 1][j][VERTICAL] += dp[i][j][VERTICAL]
            if (
                i + 1 < n
                and j + 1 < n
                and home[i + 1][j] == 0
                and home[i][j + 1] == 0
                and home[i + 1][j + 1] == 0
            ):
                dp[i + 1][j + 1][DIAGONAL] += dp[i][j][VERTICAL]
        if dp[i][j][DIAGONAL]:
            if j + 1 < n and home[i][j + 1] == 0:
                dp[i][j + 1][HORIZONTAL] += dp[i][j][DIAGONAL]
            if i + 1 < n and home[i + 1][j] == 0:
                dp[i + 1][j][VERTICAL] += dp[i][j][DIAGONAL]
            if (
                i + 1 < n
                and j + 1 < n
                and home[i + 1][j] == 0
                and home[i][j + 1] == 0
                and home[i + 1][j + 1] == 0
            ):
                dp[i + 1][j + 1][DIAGONAL] += dp[i][j][DIAGONAL]

print(sum(dp[n - 1][n - 1]))
