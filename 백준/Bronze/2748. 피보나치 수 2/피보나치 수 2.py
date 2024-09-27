from sys import stdin

input = stdin.readline


def divide_conquer(n):
    if n == 1:
        return (1, 1, 0)
    a0, a1, a2 = divide_conquer(n // 2)
    n0 = (a0**2) + (a1**2)
    n1 = (a0 * a1) + (a1 * a2)
    n2 = (a1**2) + (a2**2)
    if n % 2 == 0:
        return (n0, n1, n2)
    else:
        return ((n0 + n1), n0, n1)


n = int(input())
if n == 1:
    print(1)
else:
    ans, _, _ = divide_conquer(n - 1)
    print(ans)
