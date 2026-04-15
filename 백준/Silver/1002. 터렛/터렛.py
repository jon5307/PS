from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    a, b, c, d, e, f = map(int, input().rstrip().split())
    distance = ((a - d) ** 2 + (b - e) ** 2) ** (1 / 2)
    if distance == 0 and c == f:
        print(-1)
    elif abs(c - f) == distance or c + f == distance:
        print(1)
    elif abs(c - f) < distance < (c + f):
        print(2)
    else:
        print(0)
