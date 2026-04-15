from sys import stdin
from bisect import bisect_left

input = stdin.readline


n = int(input())
arr = list(map(int, input().rstrip().split()))
dp = []
for value in arr:
    idx = bisect_left(dp, value)
    if idx == len(dp):
        dp.append(value)
    else:
        dp[idx] = value
print(len(dp))
