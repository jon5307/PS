from sys import stdin
input = stdin.readline


def one_two_three(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return one_two_three(n-1) + one_two_three(n-2) + one_two_three(n-3)

for _ in range(int(input())):
    print(one_two_three(int(input())))
