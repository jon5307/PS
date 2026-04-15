from sys import stdin

input = stdin.readline

a = []
for _ in range(3):
    a.append(int(input()))

a.sort()
print(a[1])
