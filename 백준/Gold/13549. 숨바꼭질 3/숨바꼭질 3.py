from sys import stdin
from collections import deque

input = stdin.readline


def main():
    n, k = map(int, input().rstrip().split())

    visited = set()
    queue = deque()
    queue.append((n, 0))

    while queue:
        current, time = queue.popleft()
        if current == k:
            print(time)
            return
        visited.add(current)
        if current != 0 and not (current - 1 in visited):
            queue.append((current - 1, time + 1))
        if current != 100000 and not (current + 1 in visited):
            queue.append((current + 1, time + 1))
        if current <= 50000 and not (2 * current in visited):
            queue.appendleft((2 * current, time))


main()
