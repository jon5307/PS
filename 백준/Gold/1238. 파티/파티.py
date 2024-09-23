from sys import stdin
import heapq

input = stdin.readline
maxsize = 1000000

n, m, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
r_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    r_graph[b].append((a, c))


# 가는데 걸리는 시간 계산
go = [maxsize for _ in range(n + 1)]
go[x] = 0
visited = [False for _ in range(n + 1)]

hq = []
heapq.heappush(hq, (0, x))
while hq:
    da, a = heapq.heappop(hq)
    for b, w in r_graph[a]:
        if da + w < go[b]:
            go[b] = da + w
            heapq.heappush(hq, (go[b], b))
    visited[a] = True

# 오는데 걸리는 시간 계산
back = [maxsize for _ in range(n + 1)]
back[x] = 0
visited = [False for _ in range(n + 1)]

hq = []
heapq.heappush(hq, (0, x))
while hq:
    da, a = heapq.heappop(hq)
    for b, w in graph[a]:
        if da + w < back[b]:
            back[b] = da + w
            heapq.heappush(hq, (back[b], b))
    visited[a] = True

timemax = 0
for i in range(1, n + 1):
    if go[i] + back[i] > timemax:
        timemax = go[i] + back[i]
print(timemax)
