from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
num = list(map(int,input().split()))
total = 0
sum = [0]
for i in range(n):
    total += num[i]
    sum.append(total)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j]-sum[i-1])
