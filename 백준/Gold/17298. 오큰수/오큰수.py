from sys import stdin
import heapq
from collections import deque

input = stdin.readline

n = int(input())
nge = [-1] * n
heap = []
queue = deque()

for e in map(int, input().rstrip().split()):
    queue.append(e)

for i in range(n):
    a = queue.popleft()
    while len(heap) != 0 and heap[0][0] < a:
        b, idx = heapq.heappop(heap)
        nge[idx] = a
    heapq.heappush(heap, (a, i))

print(*nge)
