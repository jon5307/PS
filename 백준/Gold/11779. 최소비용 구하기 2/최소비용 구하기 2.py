from sys import stdin
import heapq

input = stdin.readline
MAX = 10**8

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
route = [[i] for i in range(n + 1)]
distance = [MAX for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
start, dest = map(int, input().rstrip().split())

distance[start] = 0
hq = []
heapq.heappush(hq, (0, start))
while hq:
    da, a = heapq.heappop(hq)
    if da > distance[a]:
        continue
    for b, w in graph[a]:
        if da + w < distance[b]:
            distance[b] = da + w
            heapq.heappush(hq, (distance[b], b))
            route[b] = route[a] + [b]

print(distance[dest])
print(len(route[dest]))
print(*route[dest], sep=" ")
