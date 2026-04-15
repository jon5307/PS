from sys import stdin

input = stdin.readline
INF = 200000000


def detect_negative_cycle(n, edges):
    distance = [INF] * (n + 1)
    distance[1] = 0
    for _ in range(n):
        for s, e, c in edges:
            if distance[s] + c < distance[e]:
                distance[e] = distance[s] + c
    for s, e, c in edges:
        if distance[s] + c < distance[e]:
            return True
    return False


def wormhole():
    n, m, w = map(int, input().rstrip().split())
    edges = []
    for _ in range(m):
        s, e, c = map(int, input().rstrip().split())
        edges.append((s, e, c))
        edges.append((e, s, c))
    for _ in range(w):
        s, e, c = map(int, input().rstrip().split())
        edges.append((s, e, -c))
    return detect_negative_cycle(n, edges)


for _ in range(int(input())):
    if wormhole():
        print("YES")
    else:
        print("NO")
