import sys
import math

case_num = 1
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break

    print(f"Triangle #{case_num}")

    if c == -1:  # 빗변을 구해야 하는 경우
        c = math.sqrt(a**2 + b**2)
        print(f"c = {c:.3f}\n")
    elif a == -1:  # 밑변을 구해야 하는 경우
        if c > b:
            a = math.sqrt(c**2 - b**2)
            print(f"a = {a:.3f}\n")
        else:
            print("Impossible.\n")
    elif b == -1:  # 높이를 구해야 하는 경우
        if c > a:
            b = math.sqrt(c**2 - a**2)
            print(f"b = {b:.3f}\n")
        else:
            print("Impossible.\n")

    case_num += 1