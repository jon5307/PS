n = int(input())

t = []
for _ in range(n):
    t += list(map(int, input().split()))

tri_len = n * (n + 1) // 2

dp = [0 for _ in range(tri_len)]

for i in range(tri_len - 1, tri_len - 1 - n, -1):
    dp[i] = t[i]

end = tri_len - 1 - n
width = n - 1
while width > 0:
    for i in range(end, end - width, -1):
        dp[i] = max(dp[i + width + 1], dp[i + width]) + t[i]
    end -= width
    width -= 1

print(dp[0])
