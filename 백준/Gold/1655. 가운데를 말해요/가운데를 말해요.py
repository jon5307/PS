from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

low_to_mid = []
mid_to_high = []

for i in range(int(input())):
    num = int(input())
    if i == 0:
        heappush(low_to_mid, -num)
        print(num)
        continue
    elif i % 2 == 0:
        if num <= mid_to_high[0]:
            heappush(low_to_mid, -num)
        else:
            heappush(low_to_mid, -heappop(mid_to_high))
            heappush(mid_to_high, num)
    else:
        if -low_to_mid[0] <= num:
            heappush(mid_to_high, num)
        else:
            heappush(mid_to_high, -heappop(low_to_mid))
            heappush(low_to_mid, -num)
    print(min(-low_to_mid[0], mid_to_high[0]))
