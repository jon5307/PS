from sys import stdin
from math import gcd

nums = []
for line in stdin:
    nums += list(map(int, line.split()))

max_gcd = 0
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        max_gcd = max(max_gcd, gcd(nums[i], nums[j]))

print(max_gcd)