from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


def is_same_subtree(a, b):
    return find(a) == find(b)


def union_subtree(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        if rank[a_root] < rank[b_root]:
            parent[a_root] = b_root
        elif rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
        else:
            parent[b_root] = a_root
            rank[a_root] += 1


N = int(input())
parent = [i for i in range(N)]
rank = [0] * (N)
planet = [[] for _ in range(3)]

for i in range(N):
    for axis, coord in enumerate(map(int, input().rstrip().split())):
        planet[axis].append((coord, i))

for i in range(3):
    planet[i].sort()

heap = []
for axis_planet in planet:
    for i in range(N - 1):
        heappush(
            heap,
            (
                axis_planet[i + 1][0] - axis_planet[i][0],
                axis_planet[i + 1][1],
                axis_planet[i][1],
            ),
        )

mst_edges = []

while len(mst_edges) < N - 1:
    d, s, e = heappop(heap)
    if is_same_subtree(s, e):
        continue
    union_subtree(s, e)
    mst_edges.append(d)

print(sum(mst_edges))
