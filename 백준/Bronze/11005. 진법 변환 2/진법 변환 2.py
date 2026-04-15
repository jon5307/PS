from sys import stdin

input = stdin.readline


n, b = map(int, input().split())
base = [str(i) for i in range(b if b <= 10 else 10)]
for i in range(10, b):
    base.append(chr(ord("A") + i - 10))
converted = []
while n > 0:
    converted.append(base[n % b])
    n //= b

print(*converted[::-1], sep="")
