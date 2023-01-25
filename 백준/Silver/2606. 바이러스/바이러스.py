from sys import stdin
input = stdin.readline
from collections import deque

def worm(network, pcs):
    virus = [ False for _ in range(pcs) ]
    que = deque([0])
    while len(que) != 0:
        head = que.popleft()
        virus[head] = True    
        for i in range(pcs):
            if not virus[i] and network[head][i]:
                que.append(i)
    return virus

pcs = int(input())

network = [ [False for _ in range(pcs)] for _ in range(pcs) ]
for _ in range(int(input())):
    x, y = map(int,input().split())
    network[x-1][y-1] = True
    network[y-1][x-1] = True

virus = worm(network, pcs)
print(sum(virus)-1)
