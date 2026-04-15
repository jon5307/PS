from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())
print(min(n // 2, m // 2))
