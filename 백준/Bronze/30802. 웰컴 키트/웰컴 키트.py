from sys import stdin
import math

input = stdin.readline

n = int(input())
shirt = list(map(int, input().split()))
t, p = map(int, input().split())

t_set = 0
for i in shirt:
    t_set += math.ceil(i / t)

print(t_set)
print(n // p, n % p)
