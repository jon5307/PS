from sys import stdin

input = stdin.readline

input()
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = []
a_idx = 0
b_idx = 0
while a_idx < len(a) and b_idx < len(b):
    if a[a_idx] < b[b_idx]:
        result.append(a[a_idx])
        a_idx += 1
    else:
        result.append(b[b_idx])
        b_idx += 1
if a_idx == len(a):
    result.extend(b[b_idx:])
else:
    result.extend(a[a_idx:])
print(*result)
