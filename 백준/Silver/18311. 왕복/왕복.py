from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())
d = 0
course = list(map(int, input().rstrip().split()))
for idx, i in enumerate(course):
    d += i
    if k < d:
        print(idx + 1)
        exit(0)
for idx, i in enumerate(course[::-1]):
    d += i
    if k < d:
        print(n - idx)
        exit(0)
