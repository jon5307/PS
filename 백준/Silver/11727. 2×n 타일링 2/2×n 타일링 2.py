def two_by_n(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 3

        for i in range(2,n):
            dp[i] = (dp[i-1] + 2*dp[i-2]) % 10007

        return dp[n-1]

print(two_by_n(int(input())))
