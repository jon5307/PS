from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())

nums = []
for num in map(int, input().rstrip().split()):
    if not num in nums:
        nums.append(num)

nums.sort()


def dfs(depth, seq):
    if depth > m:
        print(*seq)
    elif depth == 1:
        for num in nums:
            dfs(depth + 1, [num])
    else:
        for num in nums:
            if seq[-1] <= num:
                dfs(depth + 1, seq + [num])


dfs(1, [])
