from sys import stdin
from collections import deque

input = stdin.readline

v, e = map(int, input().rstrip().split())
indegree = [0 for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    start, end = map(int, input().rstrip().split())
    graph[start].append(end)
    indegree[end] += 1

queue = deque()
result = []
for i in range(1, v + 1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    now = queue.popleft()
    result.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
print(*result)
