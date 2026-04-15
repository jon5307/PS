from sys import stdin

input = stdin.readline


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


for _ in range(int(input())):
    parent = {}
    rank = {}
    count = {}
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if a not in parent:
            parent[a] = a
            rank[a] = 0
            count[a] = 1
        if b not in parent:
            parent[b] = b
            rank[b] = 0
            count[b] = 1
        a_root = find(a)
        b_root = find(b)
        if a_root != b_root:
            if rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
                count[b_root] += count[a_root]
                rank[b_root] += 1
                print(count[b_root])
            else:
                parent[b_root] = a_root
                count[a_root] += count[b_root]
                rank[a_root] += 1
                print(count[a_root])
        else:
            print(count[a_root])
