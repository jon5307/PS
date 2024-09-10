from sys import stdin

input = stdin.readline

N = int(input())
jul = []
max_dp = []
min_dp = []

first_line = list(map(int, input().split()))

max_dp.append(first_line[:])
max_dp.append([0, 0, 0])
min_dp.append(first_line[:])
min_dp.append([0, 0, 0])

for i in range(1, N):
    next_line = list(map(int, input().split()))
    max_dp[1][0] = next_line[0] + max(max_dp[0][0:2])
    max_dp[1][1] = next_line[1] + max(max_dp[0][0:3])
    max_dp[1][2] = next_line[2] + max(max_dp[0][1:3])
    max_dp[0][0] = max_dp[1][0]
    max_dp[0][1] = max_dp[1][1]
    max_dp[0][2] = max_dp[1][2]
    min_dp[1][0] = next_line[0] + min(min_dp[0][0:2])
    min_dp[1][1] = next_line[1] + min(min_dp[0][0:3])
    min_dp[1][2] = next_line[2] + min(min_dp[0][1:3])
    min_dp[0][0] = min_dp[1][0]
    min_dp[0][1] = min_dp[1][1]
    min_dp[0][2] = min_dp[1][2]

print(max(max_dp[0]), min(min_dp[0]))
