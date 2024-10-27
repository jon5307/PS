import heapq
from sys import stdin

input = stdin.readline

n = int(input())
value = [0] + list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    a, b = map(int, input().rstrip().split())
    graph[a].append((i + 1, b))


def cut(node):
    count = 1
    for child, _ in graph[node]:
        count += cut(child)
    return count


def dfs(node, max_dist):
    count = 0
    for child, dist in graph[node]:
        if value[child] < max_dist + dist:
            count += cut(child)
        else:
            count += dfs(child, max_dist + dist)
    return count


print(dfs(1, 0))
