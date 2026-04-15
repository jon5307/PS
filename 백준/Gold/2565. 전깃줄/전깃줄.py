from sys import stdin
import heapq

input = stdin.readline


heap = []
n = int(input())
for _ in range(n):
    heapq.heappush(heap, tuple(map(int, input().rstrip().split())))

arr = []
for _ in range(n):
    _, a = heapq.heappop(heap)
    arr.append(a)

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(n - max(dp))
