from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    a, b = input().rstrip().split()
    c = 0
    d = 0
    for i in range(len(a)):
        c += (10**i) * int(a[i])
    for i in range(len(b)):
        d += (10**i) * int(b[i])
    e = str(c + d)
    print_zero = False
    for i in range(len(e) - 1, -1, -1):
        if e[i] == "0" and not print_zero:
            continue
        else:
            print(e[i], end="")
            print_zero = True
    if int(e) == 0:
        print("0")
    else:
        print()
