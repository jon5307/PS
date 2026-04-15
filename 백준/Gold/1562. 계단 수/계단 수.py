from sys import stdin

input = stdin.readline

n = int(input())

dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n)]
for i in range(1, 10):
    dp[0][i][1 << i] = 1

for length in range(1, n):
    for num in range(10):
        for bitmask in range(1 << 10):
            if num - 1 >= 0:
                dp[length][num][bitmask | (1 << num)] += dp[length - 1][num - 1][
                    bitmask
                ]
            if num + 1 <= 9:
                dp[length][num][bitmask | (1 << num)] += dp[length - 1][num + 1][
                    bitmask
                ]
            dp[length][num][bitmask | (1 << num)] %= 1000000000

res = 0
for k in range(10):
    res += dp[n - 1][k][1023]
print(res % 1000000000)
