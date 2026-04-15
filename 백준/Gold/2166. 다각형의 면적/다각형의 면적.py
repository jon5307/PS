from sys import stdin

input = stdin.readline

n = int(input())

dots = []

for _ in range(n):
    dots.append(list(map(int, input().rstrip().split())))

sum = 0
for i in range(n):
    sum += (dots[(i) % n][0] + dots[(i + 1) % n][0]) * (
        dots[(i) % n][1] - dots[(i + 1) % n][1]
    )

print(round(abs(sum) / 2, 1))
