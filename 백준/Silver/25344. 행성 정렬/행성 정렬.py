from sys import stdin
from math import gcd

input = stdin.readline


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
times = list(map(int, input().split()))

answer = times[0]
for t in times[1:]:
    answer = lcm(answer, t)

print(answer)
