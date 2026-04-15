from sys import stdin

input = stdin.readline


def find_root(node):
    if node != parent[node]:
        parent[node] = find_root(parent[node])
    return parent[node]


n, m = map(int, input().rstrip().split())
parent = [i for i in range(n)]
child = [None for _ in range(n)]
rank = [0] * (n)

for i in range(m):
    a, b = map(int, input().rstrip().split())
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
    else:
        print(i + 1)
        exit(0)
print(0)
