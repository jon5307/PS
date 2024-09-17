from sys import stdin
from collections import deque

input = stdin.readline


def d(i):
    return (2 * i) % 10000


def s(i):
    return (i - 1) % 10000


def l(i):
    return (i % 1000) * 10 + i // 1000


def r(i):
    return (i // 10) + (i % 10) * 1000


def bfs(start, goal):
    queue = deque([start])
    parents = {start: None}
    while queue:
        node = queue.popleft()
        if node == goal:
            path = []
            while parents[node] != None:
                path.append(parents[node][1])
                node = parents[node][0]
            return path[::-1]
        else:
            neighbor = d(node)
            if neighbor not in parents:
                queue.append(neighbor)
                parents[neighbor] = [node, "D"]
            neighbor = s(node)
            if neighbor not in parents:
                queue.append(neighbor)
                parents[neighbor] = [node, "S"]
            neighbor = l(node)
            if neighbor not in parents:
                queue.append(neighbor)
                parents[neighbor] = [node, "L"]
            neighbor = r(node)
            if neighbor not in parents:
                queue.append(neighbor)
                parents[neighbor] = [node, "R"]
    return None


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(*bfs(a, b), sep="")
