from math import ceil

a, b = map(int, input().rstrip().split())
d = int(input())

print(ceil(a * b / 12) * d)
