from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().rstrip().split())

queue = deque((n,))
visited = set((n,))
time = 0
dist = [-1] * 100001
while queue:
    for _ in range(len(queue)):
        a = queue.popleft()
        if a == k:
            print(time)
            arr = []
            while a != -1:
                arr.append(a)
                a = dist[a]
            print(" ".join(map(str, arr[::-1])))
            exit(0)
        for b in (a - 1, a + 1, 2 * a):
            if 0 <= b <= 100000 and b not in visited:
                dist[b] = a
                queue.append(b)
                visited.add(b)
    time += 1
