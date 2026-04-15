from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

n, m = map(int, input().rstrip().split())

indegree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

queue = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heappush(queue, i)

while queue:
    p = heappop(queue)
    for q in graph[p]:
        indegree[q] -= 1
        if indegree[q] == 0:
            heappush(queue, q)
    print(p, end=" ")
