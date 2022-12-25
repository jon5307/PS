loop = int(input())
list = input().split(" ")
small, big = 1000000, -1000000
for i in range(loop):
    small = min(small, int(list[i]))
for i in range(loop):
    big = max(big, int(list[i]))
print("%d %d" %(small, big))