from sys import stdin
input = stdin.readline


n,m = map(int, input().split())
graph = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True

cc_amount = 0
linked = [False for _ in range(n)]
for i in range(n):
    if not linked[i]:
        linked[i] = True
        queue = [i]
        while queue:
            a = queue.pop(0)
            for j in range(n):
                if graph[a][j] and not linked[j]:
                    linked[j] = True
                    queue.append(j)
        cc_amount += 1

print(cc_amount)
