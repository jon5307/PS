from sys import stdin

input = stdin.readline


n, k = map(int, input().rstrip().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]

dp[0] = 1

for coin in coins:
    for price in range(coin, k + 1):
        dp[price] += dp[price - coin]

print(dp[k])
