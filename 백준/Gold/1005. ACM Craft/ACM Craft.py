from sys import stdin
from collections import deque

input = stdin.readline

for T in range(int(input())):
    N, K = map(int, input().rstrip().split())
    D = list(map(int, input().rstrip().split()))
    indegree = [0 for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().rstrip().split())
        graph[X].append(Y)
        indegree[Y] += 1
    goal = int(input())
    dp = [0] + [D[i] for i in range(N)]
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            dp[i] = max(dp[i], dp[node] + D[i - 1])
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    print(dp[goal])
