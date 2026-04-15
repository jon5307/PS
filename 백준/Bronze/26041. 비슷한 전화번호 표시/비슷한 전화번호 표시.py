from sys import stdin

input = stdin.readline


pb = list(input().rstrip().split())
p = input().rstrip()
c = 0
for a in pb:
    if len(a) > len(p) and a[: len(p)] == p:
        c += 1

print(c)
