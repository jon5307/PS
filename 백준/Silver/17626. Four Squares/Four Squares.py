from sys import stdin
from math import sqrt

input = stdin.readline


n = int(input())
sqrs = [i**2 for i in range(int(sqrt(n)) + 1)]

dp = [5] * (n + 1)
dp[0] = 0
for i in range(n + 1):
    for sqr in sqrs:
        if sqr + i <= n:
            dp[sqr + i] = min(dp[sqr + i], dp[i] + 1)
print(dp[n])
