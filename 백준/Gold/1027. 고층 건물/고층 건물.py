from sys import stdin

input = stdin.readline


def check(building, my_height):
    min_grad = -1000000001
    max_view = 0
    for d, h in enumerate(building):
        cur_grad = (h - my_height) / (d + 1)
        if min_grad < cur_grad:
            min_grad = cur_grad
            max_view += 1
    return max_view


n = int(input())
building = list(map(int, input().rstrip().split()))
max_view = 0
for i in range(n):
    left_view = check(building[i - 1 :: -1], building[i]) if i > 0 else 0
    right_view = check(building[i + 1 :], building[i]) if i < n - 1 else 0
    max_view = max(max_view, left_view + right_view)
print(max_view)
