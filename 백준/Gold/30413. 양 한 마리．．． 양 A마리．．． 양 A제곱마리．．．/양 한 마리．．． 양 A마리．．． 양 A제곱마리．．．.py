mod = 1000000007


def mod_inv(b):
    return pow(b, mod - 2, mod)


a, b = map(int, input().rstrip().split())
if a == 1:
    print(b%mod)
elif b == 1:
    print(1)
else:
    child = pow(a, b, mod) - 1
    parent = a - 1
    print((child * mod_inv(parent)) % mod)
