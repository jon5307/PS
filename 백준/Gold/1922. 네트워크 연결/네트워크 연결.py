from sys import stdin
import heapq

input = stdin.readline


def find_root(node):
    if node != parent[node]:
        parent[node] = find_root(parent[node])
    return parent[node]


def is_same_subtree(a, b):
    return find_root(a) == find_root(b)


def union_subtree(a, b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        if rank[a_root] < rank[b_root]:
            parent[a_root] = b_root
        elif rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
        else:
            parent[b_root] = a_root
            rank[a_root] += 1


v = int(input())
e = int(input())
graph = []
for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    heapq.heappush(graph, (c, a, b))

mst_edges = []
parent = [i for i in range(v + 1)]
rank = [0] * (v + 1)


while len(mst_edges) < v - 1:
    c, a, b = heapq.heappop(graph)
    if is_same_subtree(a, b):
        continue
    union_subtree(a, b)
    mst_edges.append(c)


print(sum(mst_edges))
