from sys import stdin

input = stdin.readline

n = int(input())

cost = []
for _ in range(n):
    cost.append(list(map(int, input().rstrip().split())))

min_value = 1000000
for first_color in range(3):
    dp = [[0] * 3 for _ in range(n)]
    for i in range(3):
        if first_color == i:
            dp[0][first_color] = cost[0][first_color]
        else:
            dp[0][i] = 1000000

    for i in range(1, n - 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        if dp[i][0] > 1000000:
            dp[i][0] = 1000000
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        if dp[i][1] > 1000000:
            dp[i][1] = 1000000
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + cost[i][2]
        if dp[i][2] > 1000000:
            dp[i][2] = 1000000

    if first_color != 0:
        dp[n - 1][0] = min(dp[n - 2][1], dp[n - 2][2]) + cost[n - 1][0]
    else:
        dp[n - 1][0] = 1000000
    if first_color != 1:
        dp[n - 1][1] = min(dp[n - 2][0], dp[n - 2][2]) + cost[n - 1][1]
    else:
        dp[n - 1][1] = 1000000
    if first_color != 2:
        dp[n - 1][2] = min(dp[n - 2][1], dp[n - 2][0]) + cost[n - 1][2]
    else:
        dp[n - 1][2] = 1000000
    min_value = min(min_value, min(dp[n - 1]))
print(min_value)