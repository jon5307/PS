import sys
input = sys.stdin.readline

loc = []
for _ in range(int(input())):
    loc.append(tuple(map(int,input().split())))

loc.sort()

for i in loc:
    print(i[0],i[1])
