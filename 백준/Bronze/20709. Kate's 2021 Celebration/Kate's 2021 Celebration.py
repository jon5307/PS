from sys import stdin

input = stdin.readline

MAX = 10**5 + 1
min_idx = 0
min_cost = MAX
for i in range(int(input())):
    cost, ballon = input().rstrip().split()
    cost = int(cost)
    c2 = str(ballon).count("2")
    c0 = str(ballon).count("0")
    c1 = str(ballon).count("1")
    if c2 >= 2 and c0 >= 1 and c1 >= 1 and min_cost > cost:
        min_idx = i + 1
        min_cost = cost

if min_cost == MAX:
    print(0)
else:
    print(min_idx)
