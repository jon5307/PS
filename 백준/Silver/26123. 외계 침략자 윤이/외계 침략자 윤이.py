n, d = map(int, input().split())

building = list(map(int, input().split()))

h = max(building) - d
if h < 0:
    h = 0

sum = 0
for i in building:
    a = i - h
    if a > 0:
        sum += a
print(sum)
