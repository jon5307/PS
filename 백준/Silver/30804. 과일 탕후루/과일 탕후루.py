from sys import stdin

input = stdin.readline


n = int(input())
fruit = list(map(int, input().rstrip().split()))

max_fruit = 1
start = 0
use = {fruit[start]: 1}
for end in range(start + 1, n):
    if fruit[end] in use:
        use[fruit[end]] += 1
    else:
        use[fruit[end]] = 1
    if len(use) > 2:
        if use[fruit[start]] == 1:
            del use[fruit[start]]
        else:
            use[fruit[start]] -= 1
        start += 1
    max_fruit = max(max_fruit, end - start + 1)

print(max_fruit)
