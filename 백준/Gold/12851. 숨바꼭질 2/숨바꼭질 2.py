from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().rstrip().split())

if n == k:
    print(0, 1, sep="\n")
else:
    visited = set()
    queue = deque()
    queue.append(n)
    distance = 1
    while queue:
        path_count = 0
        current_visited = set()
        for _ in range(len(queue)):
            a = queue.popleft()
            for b in (a + 1, a - 1, 2 * a):
                if b == k:
                    path_count += 1
                elif 0 <= b <= 100000 and not b in visited:
                    queue.append(b)
                    current_visited.add(b)
        if path_count > 0:
            break
        distance += 1
        for i in current_visited:
            visited.add(i)
    print(distance, path_count, sep="\n")
