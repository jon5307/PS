from sys import stdin
import bisect

input = stdin.readline

n = int(input())
arrs = [[] for _ in range(4)]
for _ in range(n):
    a, b, c, d = map(int, input().rstrip().split())
    arrs[0].append(a)
    arrs[1].append(b)
    arrs[2].append(c)
    arrs[3].append(d)

sum_dict = {}

for a in arrs[0]:
    for b in arrs[1]:
        sum_ab = a + b
        if sum_ab in sum_dict:
            sum_dict[sum_ab] += 1
        else:
            sum_dict[sum_ab] = 1

pair_count = 0

for c in arrs[2]:
    for d in arrs[3]:
        sum_cd = -(c + d)
        if sum_cd in sum_dict:
            pair_count += sum_dict[sum_cd]

print(pair_count)
