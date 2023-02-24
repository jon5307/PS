from sys import stdin
input = stdin.readline


def solve():
    n = int(input())
    cloth = {}
    for _ in range(n):
        _, kind = input().split()
        if kind in cloth:
            cloth[kind] += 1
        else:
            cloth[kind] = 1
    ans = 1
    for i in cloth.values():
        ans *= i+1
    print(ans-1)

for _ in range(int(input())):
    solve()
    