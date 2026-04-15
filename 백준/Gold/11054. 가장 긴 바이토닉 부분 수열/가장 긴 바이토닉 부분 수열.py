from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
normal = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and normal[i] <= normal[j]:
            normal[i] = normal[j] + 1

reverse = [1 for _ in range(n)]
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i - 1, -1):
        if arr[i] > arr[j] and reverse[i] <= reverse[j]:
            reverse[i] = reverse[j] + 1

max_len = 0
for i in range(n):
    max_len = max(max_len, normal[i] + reverse[i] - 1)
    for j in range(i + 1, n):
        if arr[i] != arr[j]:
            max_len = max(max_len, normal[i] + reverse[j])
        else:
            max_len = max(max_len, normal[i] + reverse[j] - 1)

print(max_len)
