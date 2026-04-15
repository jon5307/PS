from sys import stdin

input = stdin.readline


n = int(input())
arr = list(map(int, input().rstrip().split()))

back = [-1 for _ in range(n)]
size = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and size[i] <= size[j]:
            size[i] = size[j] + 1
            back[i] = j

max_size = max(size)
max_idx = size.index(max_size)
print(max_size)
route = []
while max_idx != -1:
    route.append(arr[max_idx])
    max_idx = back[max_idx]

print(*route[::-1])
