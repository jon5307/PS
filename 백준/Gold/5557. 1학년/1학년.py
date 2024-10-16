from sys import stdin

input = stdin.readline

n = int(input())

nums = list(map(int, input().rstrip().split()))

dp = [[0 for _ in range(21)] for _ in range(n - 1)]

for idx, num in enumerate(nums[:-1]):
    if idx == 0:
        dp[idx][num] = 1
    else:
        for i in range(21):
            if i + num <= 20:
                dp[idx][i + num] += dp[idx - 1][i]
            if i - num >= 0:
                dp[idx][i - num] += dp[idx - 1][i]

print(dp[n - 2][nums[n - 1]])
