from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
nums = [0 for _ in range(10000)]
for _ in range(n):
    nums[int(input())-1] += 1
for i in range(10000):
    if not nums[i] == 0:
        for _ in range(nums[i]):
            print(i+1)
