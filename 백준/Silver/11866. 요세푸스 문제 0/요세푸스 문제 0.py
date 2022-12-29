from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque(range(1,N+1))

output = "<"
for _ in range(N):
    for _ in range(K-1):
        q.append(q.popleft())
    output += str(q.popleft()) + ", "
print(output[0:-2] + ">")
