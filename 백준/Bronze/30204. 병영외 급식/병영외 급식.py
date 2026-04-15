from sys import stdin

input = stdin.readline

n, x = map(int, input().rstrip().split())
sum = 0

for i in map(int, input().rstrip().split()):
    sum += i
    if sum % x == 0:
        sum = 0

if sum == 0:
    print(1)
else:
    print(0)
