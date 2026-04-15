from sys import stdin

input = stdin.readline


def ccw(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (
        p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1]
    )


def sign(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1


a, b, c, d = map(int, input().rstrip().split())
e, f, g, h = map(int, input().rstrip().split())
p1 = (a, b)
p2 = (c, d)
p3 = (e, f)
p4 = (g, h)
v1 = ccw(p1, p3, p4)
v2 = ccw(p2, p3, p4)
v3 = ccw(p3, p1, p2)
v4 = ccw(p4, p1, p2)

if v1 * v2 == 0 and v3 * v4 == 0:
    if p1 > p2:
        p1, p2 = p2, p1
    if p3 > p4:
        p3, p4 = p4, p3
    if p1 <= p4 and p3 <= p2:
        print(1)
    else:
        print(0)
else:
    if sign(v1) * sign(v2) <= 0 and sign(v3) * sign(v4) <= 0:
        print(1)
    else:
        print(0)
        