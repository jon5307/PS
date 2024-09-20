from sys import stdin

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

a = k
while True:
    # for i in range(1, v + 1):
    #     if d[a] + graph[a][i] < d[i]:
    #         d[i] = d[a] + graph[a][i]
    for b, w in graph[a]:
        if d[a] + w < d[b]:
            d[b] = d[a] + w
    visited[a] = True
    shortest = maxsize
    for j in range(v + 1):
        if not visited[j] and d[j] < shortest:
            shortest = d[j]
            a = j
    if shortest == maxsize:
        break

for i in range(v):
    print(d[i + 1] if d[i + 1] != maxsize else "INF")
