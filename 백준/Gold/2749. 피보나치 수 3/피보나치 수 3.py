from sys import stdin

input = stdin.readline
divider = 1000000


def divide_conquer(n):
    if n == 1:
        return (1, 1, 0)
    a0, a1, a2 = divide_conquer(n // 2)
    n0 = ((a0**2) % divider + (a1**2) % divider) % divider
    n1 = ((a0 * a1) % divider + (a1 * a2) % divider) % divider
    n2 = ((a1**2) % divider + (a2**2) % divider) % divider
    if n % 2 == 0:
        return (n0, n1, n2)
    else:
        return ((n0 + n1) % divider, n0, n1)


n = int(input())
if n == 1:
    print(1)
else:
    ans, _, _ = divide_conquer(n - 1)
    print(ans)
