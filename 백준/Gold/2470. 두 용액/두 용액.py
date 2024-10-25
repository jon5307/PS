from sys import stdin

input = stdin.readline


n = int(input())
sols = list(map(int, input().rstrip().split()))
sols.sort()


def binary_search(sol1, start, end):
    if start >= end:
        return (sol1, sols[start])
    mid = (start + end) // 2
    mix_sol = sol1 + sols[mid]
    if mix_sol == 0:
        return sol1, sols[mid]
    elif mix_sol > 0:
        return min(
            (sol1, sols[mid]),
            binary_search(sol1, start, mid - 1),
            key=lambda x: abs(x[0] + x[1]),
        )
    else:
        return min(
            (sol1, sols[mid]),
            binary_search(sol1, mid + 1, end),
            key=lambda x: abs(x[0] + x[1]),
        )


s1, s2 = 1000000001, 1000000001
for i, sol1 in enumerate(sols):
    if i == n - 1:
        break
    a, b = binary_search(sol1, i + 1, n - 1)
    if a + b == 0:
        s1, s2 = a, b
        break
    elif abs(s1 + s2) > abs(a + b):
        s1, s2 = a, b

print(s1, s2)
