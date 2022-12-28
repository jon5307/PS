import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
daily = a - b
v -= b
day = v / daily
if day.is_integer():
    print(int(day))
else:
    print(int(day) + 1)