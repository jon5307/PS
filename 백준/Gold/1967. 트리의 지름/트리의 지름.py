from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(100000)

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))


def dfs(node):
    if len(graph[node]) == 0:
        return (0, 0)
    max_depth1, max_depth2, max_diameter = 0, 0, 0
    for child, weight in graph[node]:
        depth, diameter = dfs(child)
        if depth + weight > max_depth1:
            max_depth2 = max_depth1
            max_depth1 = depth + weight
        elif depth + weight > max_depth2:
            max_depth2 = depth + weight
        max_diameter = max(max_diameter, diameter)
    max_diameter = max(max_diameter, max_depth1 + max_depth2)
    return (max_depth1, max_diameter)


print(max(dfs(1)))
