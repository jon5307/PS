from sys import stdin

input = stdin.readline

n = int(input())

graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 0 and graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

for g in graph:
    print(*g)
