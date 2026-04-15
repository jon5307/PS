from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    v, e = map(int, input().rstrip().split())
    color = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = -color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for i in range(1, v + 1):
        if color[i] == 0:
            if not bfs(i):
                return False
    return True


for _ in range(int(input())):
    print("YES" if solve() else "NO")
