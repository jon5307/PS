from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


def dfs(parent, node, visited, graph):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(parent, i, visited, graph)


dfs(parent, 1, visited, graph)

print(*parent[2:], sep="\n")
