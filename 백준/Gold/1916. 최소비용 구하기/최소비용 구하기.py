from sys import stdin
import heapq

input = stdin.readline
maxsize = 100000000

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))


k, dest = map(int, input().rstrip().split())
d = [maxsize for _ in range(n + 1)]
d[k] = 0
visited = [False for _ in range(n + 1)]

hq = []
heapq.heappush(hq, (0, k))
while hq:
    da, a = heapq.heappop(hq)
    if da > d[a]:
        continue
    for b, w in graph[a]:
        if da + w < d[b]:
            d[b] = da + w
            heapq.heappush(hq, (d[b], b))
    visited[a] = True

print(d[dest])
