from collections import deque
from sys import stdin
input = stdin.readline

n = deque()

for _ in range(int(input())):
    a = int(input())
    if a == 0:
        n.pop()
    else:
        n.append(a)

print(sum(n))