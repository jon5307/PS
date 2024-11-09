from sys import stdin
from itertools import combinations

input = stdin.readline

n, m = map(int, input().rstrip().split())
city = [list(map(int, input().rstrip().split())) for _ in range(n)]

houses = []
stores = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            stores.append((i, j))

distance = [[] for _ in range(len(stores))]

for idx, store in enumerate(stores):
    for house in houses:
        distance[idx].append(abs(store[0] - house[0]) + abs(store[1] - house[1]))

min_chicken_distance = 20000
for comb in combinations(range((len(stores))), m):
    chicken_distance = 0
    for i in range(len(houses)):
        chicken_distance += min([distance[j][i] for j in comb])
    min_chicken_distance = min(min_chicken_distance, chicken_distance)

print(min_chicken_distance)
