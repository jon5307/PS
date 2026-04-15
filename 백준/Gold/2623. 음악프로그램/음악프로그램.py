from sys import stdin
from collections import deque

input = stdin.readline


n, m = map(int, input().rstrip().split())
indegree = [0 for _ in range(n + 1)]
pds = []
for _ in range(m):
    l = list(map(int, input().rstrip().split()))
    pds.append(deque(l[1:]))
    for singer in l[2:]:
        indegree[singer] += 1

queue = deque()
order = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    order.append(current)
    for pd in pds:
        if len(pd) == 0:
            continue
        first = pd.popleft()
        if first == current:
            if len(pd) == 0:
                continue
            next = pd.popleft()
            pd.appendleft(next)
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
        else:
            pd.appendleft(first)

if len(order) == n:
    print(*order, sep="\n")
else:
    print(0)
