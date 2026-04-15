from sys import stdin

input = stdin.readline


def mod_inv(b):
    return pow(b, 1000000005, 1000000007)


child = 0
parent = 1
for _ in range(int(input())):
    n, s = map(int, input().rstrip().split())
    child = (child * n + parent * s) % 1000000007
    parent *= n
    parent %= 1000000007


print((child * mod_inv(parent)) % 1000000007)
