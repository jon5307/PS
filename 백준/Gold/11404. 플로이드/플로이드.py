from sys import stdin

input = stdin.readline

INF = 10000001

n = int(input())
m = int(input())
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = min(c, graph[a][b])

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for row in graph[1:]:
    print(*(0 if i == INF else i for i in row[1:]))
