from sys import stdin

input = stdin.readline

n = int(input())
time = 0
for idx, t in enumerate(map(int, input().rstrip().split())):
    time += t
    if idx + 1 != n:
        time += 8

print(time // 24, time % 24)
