from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)


def count_nodes(root):
    visited[root] = True
    cur = 1
    for child in graph[root]:
        if not visited[child]:
            cur += count_nodes(child)
    size[root] = cur
    return cur


n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

size = [0 for _ in range(n + 1)]
visited = [False] * (n + 1)

count_nodes(r)
for _ in range(q):
    print(size[int(input())])
