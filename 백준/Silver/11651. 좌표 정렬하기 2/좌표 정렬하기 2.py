import sys
input = sys.stdin.readline

loc = []
for _ in range(int(input())):
    x, y = map(int,input().split())
    loc.append((y,x))

loc.sort()

for i in loc:
    print(i[1],i[0])
