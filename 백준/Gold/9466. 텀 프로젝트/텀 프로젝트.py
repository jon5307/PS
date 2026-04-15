from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().rstrip().split()))
    visited = [False] * (n + 1)
    have_team = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        current_route = []
        cur = i
        while not visited[cur]:
            visited[cur] = True
            current_route.append(cur)
            cur = graph[cur]
        if cur in current_route:
            have_team += len(current_route) - current_route.index(cur)
    print(n - have_team)
