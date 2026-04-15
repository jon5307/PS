from sys import stdin

input = stdin.readline


def check_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    if check_prime(p):
        print("no")
    elif pow(a, p, p) == a % p:
        print("yes")
    else:
        print("no")
