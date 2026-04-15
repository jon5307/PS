from sys import stdin
import heapq

input = stdin.readline

n = int(input())
a = []
for i, value in enumerate(map(int, input().rstrip().split())):
    heapq.heappush(a, (-value, i))
m = int(input())
b = list(map(int, input().rstrip().split()))

lcs = []

a_start_idx, b_start_idx = 0, 0
while a:
    a_value, a_idx = heapq.heappop(a)
    a_value *= -1
    if a_idx >= a_start_idx:
        for i in range(b_start_idx, len(b)):
            if b[i] == a_value:
                lcs.append(a_value)
                a_start_idx = a_idx + 1
                b_start_idx = i + 1
                break

print(len(lcs))
print(*lcs, sep=" ")
