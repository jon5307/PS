from sys import stdin

input = stdin.readline
INF = 100000

n, k = map(int, input().rstrip().split())

coins = set()

for _ in range(n):
    coins.add(int(input()))

dp = [INF for _ in range(k + 1)]
dp[0] = 0

for i in range(k):
    for coin in coins:
        if i + coin < k + 1:
            dp[i + coin] = min(dp[i + coin], dp[i] + 1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
