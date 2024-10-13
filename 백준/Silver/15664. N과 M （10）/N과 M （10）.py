from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())

count = {}
nums = []
for num in map(int, input().rstrip().split()):
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    if not num in nums:
        nums.append(num)

nums.sort()


def dfs(depth, seq):
    if depth > m:
        print(*seq)
    else:
        for num in nums:
            if num in count and count[num] > 0 and (len(seq) == 0 or seq[-1] <= num):
                count[num] -= 1
                dfs(depth + 1, seq + [num])
                count[num] += 1


dfs(1, [])
