from collections import deque

def bfs(n, k):
    q = deque([(n, 0)])
    visited = [0] * 100001
    while q:
        x, sec = q.popleft()
        if x == k:
            return sec
        if x-1 >= 0 and not visited[x-1]:
            q.append((x-1, sec+1))
            visited[x-1] = 1
        if x+1 <= 100000 and not visited[x+1]:
            q.append((x+1, sec+1))
            visited[x+1] = 1
        if x*2 <= 100000 and not visited[x*2]:
            q.append((x*2, sec+1))
            visited[x*2] = 1
    return -1

n, k = map(int, input().split())
print(bfs(n, k))
