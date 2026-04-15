mod = 1000000007


def mod_inv(b):
    return pow(b, mod - 2, mod)


n, k = map(int, input().rstrip().split())
child = 1
parent = 1
for i in range(k):
    child = (child * (n - i)) % mod
    parent = (parent * (i + 1)) % mod

print((child * mod_inv(parent)) % mod)
