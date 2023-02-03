from sys import stdin
input = stdin.readline


n = int(input())
p = list(map(int, input().split()))
p.sort()

ans = 0
for i in range(n):
    ans += p[i] * (n-i)

print(ans)
