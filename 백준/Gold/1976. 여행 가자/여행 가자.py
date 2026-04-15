from sys import stdin

input = stdin.readline


def find_root(node):
    if node != parent[node]:
        parent[node] = find_root(parent[node])  # 경로 압축
    return parent[node]


def union(a, b):
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


n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

for a in range(n):
    for b, value in enumerate(map(int, input().split())):
        if value == 1:
            union(a, b)

plan = list(map(int, input().split()))
root = find_root(plan[0] - 1)
for p in plan[1:]:
    if root != find_root(p - 1):
        print("NO")
        exit(0)
else:
    print("YES")
