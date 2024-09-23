from sys import stdin

input = stdin.readline

a, b, c = map(int, input().rstrip().split())

a %= c
m = 1
while b > 0:
    if b % 2 == 1:
        m = (m * a) % c
    a = (a**2) % c
    b //= 2

print(m)
