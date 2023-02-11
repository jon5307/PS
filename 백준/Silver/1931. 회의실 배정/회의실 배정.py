from sys import stdin
input = stdin.readline


n = int(input())

cf = []
for _ in range(n):
    cf.append(tuple(map(int, input().split())))

cf.sort(key=lambda x:x[0])
cf.sort(key=lambda x:x[1])

count = 0
end = 0
for i in cf:
    if i[0] >= end: # conference no idx can start
        end = i[1]
        count += 1

print(count)
