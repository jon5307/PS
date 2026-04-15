from sys import stdin
from math import ceil

input = stdin.readline

T = int(input())
for case_num in range(1, T + 1):
    M, D, W = map(int, input().split())
    lines = 0
    start_col = 0
    for _ in range(M):
        last_col = start_col + D - 1
        rows = ceil((last_col + 1) / W)
        lines += rows
        start_col = (last_col + 1) % W
    print(f"Case #{case_num}: {lines}")
