from sys import stdin
input = stdin.readline
import heapq as hq


heap = []
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap,a)
