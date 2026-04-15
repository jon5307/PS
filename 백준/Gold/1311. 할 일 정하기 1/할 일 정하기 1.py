from sys import stdin

input = stdin.readline

MAX = 10000 * 20
n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[MAX for _ in range(2**n)] for _ in range(n)]
for i in range(n):
    dp[0][1 << i] = graph[0][i]
for person in range(1, n):
    for bitmask in range(2**n):
        if dp[person - 1][bitmask] != MAX:
            for work in range(n):
                work_bit = 1 << work
                if not bitmask & work_bit:
                    dp[person][bitmask | work_bit] = min(
                        dp[person][bitmask | work_bit],
                        dp[person - 1][bitmask] + graph[person][work],
                    )
print(dp[n - 1][-1])
