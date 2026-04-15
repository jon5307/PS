from sys import stdin

input = stdin.readline

x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())

if x1 == x2:
    print(x3, end=" ")
elif x1 == x3:
    print(x2, end=" ")
else:
    print(x1, end=" ")
if y1 == y2:
    print(y3)
elif y1 == y3:
    print(y2)
else:
    print(y1)
