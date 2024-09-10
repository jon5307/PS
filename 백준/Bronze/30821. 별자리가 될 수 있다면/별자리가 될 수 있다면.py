n = int(input())

ans = 1
for i in range(n - 4, n + 1):
    ans *= i

ans //= 120
print(ans)
