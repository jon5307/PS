for _ in range(int(input())):
    n = int(input())
    sti = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(len(sti[0]))] for _ in range(2)]
    dp[0][0] = sti[0][0]
    dp[1][0] = sti[1][0]
    if not n == 1:
        dp[0][1] = sti[0][1] + dp[1][0]
        dp[1][1] = sti[1][1] + dp[0][0]
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2]) + sti[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 2], dp[0][i - 2]) + sti[1][i]
    print(max(max(dp[0]), max(dp[1])))
