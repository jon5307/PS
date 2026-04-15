from sys import stdin

input = stdin.readline

x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())

dx = x2 - x1
dy = y2 - y1

if dx == 0:
    if x1 == x3:
        print(0)
    elif x1 < x3:
        print(1)
    else:
        print(-1)
elif dy == 0:
    if y1 == y3:
        print(0)
    elif y1 < y3:
        print(-1)
    else:
        print(1)
elif (x3 - x2) * dy == (y3 - y2) * dx:
    print(0)
elif (x3 - x2) * dy < (y3 - y2) * dx:
    print(1)
else:
    print(-1)
