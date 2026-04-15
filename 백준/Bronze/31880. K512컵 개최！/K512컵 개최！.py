from sys import stdin

input = stdin.readline


n, m = map(int, input().rstrip().split())
a = sum(map(int, input().rstrip().split()))
for i in map(int, input().rstrip().split()):
    if i != 0:
        a *= i

print(a)
