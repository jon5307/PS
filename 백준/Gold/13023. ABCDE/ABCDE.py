from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
friend = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)

def dfs(depth, used, cur):
    if depth == 5:
        return True
    for neighbor in friend[cur]:
        if neighbor not in used:
            used.add(neighbor)
            if dfs(depth + 1, used, neighbor):
                return True
            used.remove(neighbor)
    return False

found = False
for start in range(n):
    if dfs(1, {start}, start):
        found = True
        break

print(1 if found else 0)
