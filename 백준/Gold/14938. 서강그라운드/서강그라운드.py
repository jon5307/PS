from sys import stdin

input = stdin.readline

n, m, r = map(int, input().rstrip().split())
INF = m + 1
items = [0] + list(map(int, input().rstrip().split()))
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().rstrip().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

maximum_items_collected = 0
for i in range(1, n + 1):
    cur = 0
    for j in range(1, n + 1):
        if graph[i][j] < INF:
            cur += items[j]
    maximum_items_collected = max(maximum_items_collected, cur)

print(maximum_items_collected)
