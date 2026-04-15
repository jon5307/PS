from sys import stdin

input = stdin.readline

mod = 1000000007


def mod_inv(b):
    return pow(b, mod - 2, mod)


fac = [0 for _ in range(4000001)]
fac[1] = 1
for i in range(2, 4000001):
    fac[i] = (fac[i - 1] * (i) % mod) % mod

for _ in range(int(input())):
    n, k = map(int, input().rstrip().split())
    if k == 0 or n == k:
        print(1)
        continue
    child = fac[n]
    parent = (fac[k] * fac[n - k]) % mod
    print((child * mod_inv(parent)) % mod)
