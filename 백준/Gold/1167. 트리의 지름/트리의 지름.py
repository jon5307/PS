from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n):
    start = None
    queue = deque(map(int, input().rstrip().split()))
    while queue:
        if start == None:
            start = queue.popleft()
        else:
            end = queue.popleft()
            if end == -1:
                break
            weight = queue.popleft()
            graph[start].append((end, weight))


def dfs(node):
    if len(graph[node]) == 0:
        return (0, 0)
    max_depth1, max_depth2, max_diameter = 0, 0, 0
    visited[node] = True
    for child, weight in graph[node]:
        if not visited[child]:
            depth, diameter = dfs(child)
            if depth + weight > max_depth1:
                max_depth2 = max_depth1
                max_depth1 = depth + weight
            elif depth + weight > max_depth2:
                max_depth2 = depth + weight
            max_diameter = max(max_diameter, diameter)
    max_diameter = max(max_diameter, max_depth1 + max_depth2)
    return (max_depth1, max_diameter)


visited = [False for _ in range(n + 1)]
print(max(dfs(1)))
