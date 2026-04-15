from sys import stdin

input = stdin.readline

n = int(input())
ladder = [0] + [int(input()) for _ in range(n)]
if n == 1:
    print(ladder[1])
elif n == 2:
    print(ladder[1] + ladder[2])
elif n > 2:
    dp = [[0, 0] for _ in range(n + 1)]

    dp[1][0] = ladder[1]
    dp[1][1] = ladder[1]
    dp[2][0] = ladder[2]
    dp[2][1] = ladder[1] + ladder[2]
    for i in range(3, n + 1):
        dp[i][0] = ladder[i] + max(dp[i - 2])
        dp[i][1] = ladder[i] + dp[i - 1][0]

    print(max(dp[n]))
