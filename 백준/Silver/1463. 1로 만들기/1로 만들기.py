from sys import stdin
input = stdin.readline


n = int(input())
dp = [0 for _ in range(n+1)]
dp[n] = 1
for i in range(n,0,-1):
    step = dp[i] + 1
    if step != 1:
        if dp[i-1] == 0 or dp[i-1] > dp[i] + 1:
            dp[i-1] = step
        if i % 3 == 0 and (dp[i//3] == 0 or dp[i//3] > dp[i] + 1):
            dp[i//3] = step
        if i % 2 == 0 and (dp[i//2] == 0 or dp[i//2] > dp[i] + 1):
            dp[i//2] = step
print(dp[1]-1)
