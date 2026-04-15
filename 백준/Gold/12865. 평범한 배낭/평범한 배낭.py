from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())
stuff = []
for _ in range(n):
    stuff.append(tuple(map(int, input().rstrip().split())))

dp = [0 for _ in range(k + 1)]

for w, v in stuff:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))
