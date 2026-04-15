from sys import stdin
import heapq

input = stdin.readline


heap = []
for _ in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if len(heap) != 0:
            out = heapq.heappop(heap)
            if out % 1 == 0.5:
                print(int(-(out + 0.5)))
            else:
                print(out)
        else:
            print(0)
    else:
        value = (abs(cmd) - 0.5) if cmd < 0 else cmd
        heapq.heappush(heap, value)
