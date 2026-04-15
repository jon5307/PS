from sys import stdin

input = stdin.readline


def find_root(node):
    if node != parent[node]:
        parent[node] = find_root(parent[node])  # 경로 압축
    return parent[node]


n, m = map(int, input().rstrip().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

for _ in range(m):
    c, a, b = map(int, input().rstrip().split())
    a_root = find_root(a)
    b_root = find_root(b)
    if c == 0:
        if a_root != b_root:
            if rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
            elif rank[a_root] > rank[b_root]:
                parent[b_root] = a_root
            else:
                parent[b_root] = a_root
                rank[a_root] += 1
    else:
        if a_root == b_root:
            print("YES")
        else:
            print("NO")
