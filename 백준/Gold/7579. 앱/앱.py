from sys import stdin

input = stdin.readline
MAX = 10000

n, m = map(int, input().rstrip().split())
memory = list(map(int, input().rstrip().split()))
cost = list(map(int, input().rstrip().split()))

# 최대 비용 계산
total_cost = sum(cost)

# dp[i]: i 비용으로 확보 가능한 최대 메모리
dp = [0] * (total_cost + 1)

for i in range(n):
    mem = memory[i]
    c = cost[i]
    for j in range(total_cost, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + mem)

# 조건을 만족하는 최소 비용 찾기
for i in range(total_cost + 1):
    if dp[i] >= m:
        print(i)
        break