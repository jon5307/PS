from sys import stdin

input = stdin.readline

n = int(input())

q = [int(input()) for _ in range(n)]

max_len = 0

for i in set(q):
    before = None
    c_len = 0
    c_max_len = 0
    for j in q:
        if j == i:
            continue
        if before == j:
            c_len += 1
        elif before != j:
            c_max_len = max(c_len, c_max_len)
            c_len = 1
            before = j
    c_max_len = max(c_max_len, c_len)
    max_len = max(max_len, c_max_len)

print(max_len)
