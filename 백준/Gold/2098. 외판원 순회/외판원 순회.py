from sys import stdin

input = stdin.readline

n = int(input())
MAX = n * 1000000
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[MAX for _ in range(1 << n)] for _ in range(n)]
for i in range(1, n):
    if graph[0][i] != 0:
        dp[i][(1 << i) | 1] = graph[0][i]

for bitmask in range(1 << n):
    for last in range(n):
        if dp[last][bitmask] == MAX:
            continue
        for next_city in range(n):
            if not (1 << next_city) & bitmask and graph[last][next_city] != 0:
                new_bitmask = bitmask | 1 << next_city
                dp[next_city][new_bitmask] = min(
                    dp[next_city][new_bitmask],
                    dp[last][bitmask] + graph[last][next_city],
                )

all_visited = (1 << n) - 1
min_cost = MAX
for i in range(1, n):
    if graph[i][0] != 0:
        min_cost = min(min_cost, dp[i][all_visited] + graph[i][0])

print(min_cost)
