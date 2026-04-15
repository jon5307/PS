from sys import stdin

input = stdin.readline

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)
ddir = {"U": 0, "D": 1, "L": 2, "R": 3}


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


n, m = map(int, input().split())
parent = [i for i in range(n * m)]
rank = [0] * (n * m)

for i in range(n):
    line = input().rstrip()
    for j, direction in enumerate(line):
        a = i * m + j
        b = (i + di[ddir[direction]]) * m + j + dj[ddir[direction]]
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

safe_zone = 0
for i in range(n * m):
    safe_zone += 1 if parent[i] == i else 0
print(safe_zone)
