from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())

dp = [1 for _ in range(n + 1)]

for _ in range(k - 1):
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + dp[i]) % 1000000000

print(dp[n])
