from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().rstrip().split())

queue = deque(((n, ""),))
visited = set((n,))
time = 0

while queue:
    for _ in range(len(queue)):
        a, footprint = queue.popleft()
        if a == k:
            print(time)
            print(n, end=" ")
            for c in footprint:
                if c == "-":
                    n -= 1
                elif c == "+":
                    n += 1
                else:
                    n *= 2
                print(n, end=" ")
            exit(0)
        for b, c in ((a - 1, "-"), (a + 1, "+"), (2 * a, "*")):
            if 0 <= b <= 100000 and b not in visited:
                queue.append((b, footprint + c))
                visited.add(b)
    time += 1
