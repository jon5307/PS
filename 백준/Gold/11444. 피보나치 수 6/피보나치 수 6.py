from sys import stdin

input = stdin.readline
divider = 1000000007


def divide_conquer(n):
    if n == 1:
        return (1, 1, 0)
    elif n % 2 == 0:
        a0, a1, a2 = divide_conquer(n // 2)
        n0 = ((a0**2) % divider + (a1**2) % divider) % divider
        n1 = ((a0 * a1) % divider + (a1 * a2) % divider) % divider
        n2 = ((a1**2) % divider + (a2**2) % divider) % divider
        return (n0, n1, n2)
    else:
        a0, a1, a2 = divide_conquer(n // 2)
        n0 = ((a0**2) % divider + (a1**2) % divider) % divider
        n1 = ((a0 * a1) % divider + (a1 * a2) % divider) % divider
        n2 = ((a1**2) % divider + (a2**2) % divider) % divider
        m0 = (n0 + n1) % divider
        m1 = n0 % divider
        m2 = (n1) % divider
        return (m0, m1, m2)


n = int(input())
if n == 1:
    print(1)
else:
    ans, _, _ = divide_conquer(n - 1)
    print(ans)
