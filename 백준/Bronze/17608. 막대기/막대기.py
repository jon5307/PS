from sys import stdin

input = stdin.readline

n = int(input())
stick = [int(input()) for _ in range(n)]

max_height = 0
count = 0

for s in stick[::-1]:
    if max_height < s:
        max_height = s
        count += 1

print(count)