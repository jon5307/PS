from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def solve():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    prev = 0

    for x in arr:
        mirrored = n - x + 1
        if min(x, mirrored) >= prev:
            prev = min(x, mirrored)
        elif max(x, mirrored) >= prev:
            prev = max(x, mirrored)
        else:
            print("NO\n")
            return

    print("YES\n")


for _ in range(int(input())):
    solve()
