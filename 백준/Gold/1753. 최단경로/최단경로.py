from sys import stdin
import heapq

input = stdin.readline
maxsize = 200000

v, e = map(int, input().rstrip().split())
graph = [[] for _ in range(v + 1)]

k = int(input())

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))


d = [maxsize for _ in range(v + 1)]
d[k] = 0
visited = [False for _ in range(v + 1)]

hq = []
heapq.heappush(hq, (0, k))
while hq:
    # for i in range(1, v + 1):
    #     if d[a] + graph[a][i] < d[i]:
    #         d[i] = d[a] + graph[a][i]
    da, a = heapq.heappop(hq)
    for b, w in graph[a]:
        if da + w < d[b]:
            d[b] = da + w
            heapq.heappush(hq, (d[b], b))
    visited[a] = True

for i in range(v):
    print(d[i + 1] if d[i + 1] != maxsize else "INF")
