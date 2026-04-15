from sys import stdin
import heapq

input = stdin.readline


n = int(input())
classes = []
for _ in range(n):
    classes.append(tuple(map(int, input().split())))
classes.sort()

end = [classes[0][1]]
for i in range(1, n):
    if classes[i][0] < end[0]:
        heapq.heappush(end, classes[i][1])
    else:
        heapq.heappop(end)
        heapq.heappush(end, classes[i][1])

print(len(end))
