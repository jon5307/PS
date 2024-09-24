from sys import stdin
from decimal import Decimal, ROUND_HALF_UP, getcontext

input = stdin.readline
dc = Decimal
getcontext().prec = 100


def main():
    n = int(input())

    if n == 0:
        print(0)
        return

    o = [int(input()) for _ in range(n)]

    o.sort()

    cut = int((n * dc("0.15")).quantize(dc("1."), rounding=ROUND_HALF_UP))

    d = dc(sum(o[cut : n - cut])) / dc(n - 2 * cut)

    print(d.quantize(dc("1."), rounding=ROUND_HALF_UP))
    return


main()
