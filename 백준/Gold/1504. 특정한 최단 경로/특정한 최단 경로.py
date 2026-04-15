from sys import stdin
import heapq

input = stdin.readline
MAX = 10000000

n, e = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())


def dj(s):
    distance = [MAX] * (n + 1)
    distance[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))
    while hq:
        d, now = heapq.heappop(hq)
        for next, weight in graph[now]:
            if d + weight < distance[next]:
                distance[next] = d + weight
                heapq.heappush(hq, (distance[next], next))
    return distance


start_distance = dj(1)
v1_distance = dj(v1)
v2_distance = dj(v2)

s12e = start_distance[v1] + v1_distance[v2] + v2_distance[n]
s21e = start_distance[v2] + v2_distance[v1] + v1_distance[n]
se = min(s12e, s21e)
print(se if se < MAX else -1)
