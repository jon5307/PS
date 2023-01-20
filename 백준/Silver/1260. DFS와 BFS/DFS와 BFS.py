from sys import stdin
from collections import deque
input = stdin.readline

def dfs(v, visit):
    global graph, n
    visit[v] = True
    yield v+1
    for i in range(n):
        if not visit[i] and graph[v][i]:
            yield from dfs(i, visit)     
    
def bfs(n, visit, q:deque):
    while len(q) != 0:
        v = q.popleft()
        yield v+1
        visit[v] = True
        for i in range(n):
            if visit[i] == False and graph[v][i] == True:
                q.append(i)
                visit[i] = True

n,m,v = map(int,input().split())
graph = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x-1][y-1] = True
    graph[y-1][x-1] = True


print(*dfs(v-1, [False for _ in range(n)]))
print(*bfs(n, [False for _ in range(n)], deque([v-1])))
