from sys import stdin
import heapq

input = stdin.readline


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def is_same_parent(a, b):
    return find(a) == find(b)


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b
            if rank[a] == rank[b]:
                rank[b] += 1


n = int(input())
star = []
for _ in range(n):
    # 실수 좌표를 입력받는다.
    x, y = map(float, input().split())
    # 소수점 6자리까지 반올림한다.
    star.append((x, y))

mst_edges = []
heap = []
parent = [i for i in range(n)]
rank = [0] * n

for end in range(n):
    for start in range(end):
        dist = (
            (star[start][0] - star[end][0]) ** 2 + (star[start][1] - star[end][1]) ** 2
        ) ** 0.5
        heapq.heappush(heap, (dist, start, end))

while len(mst_edges) < n - 1:
    dist, start, end = heapq.heappop(heap)
    if not is_same_parent(start, end):
        union(start, end)
        mst_edges.append(dist)

print(sum(mst_edges))
