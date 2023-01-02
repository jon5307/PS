from sys import stdin
input = stdin.readline
from itertools import combinations

N,M = map(int,input().split())
cards = list(map(int, input().split()))

max = 0
for i in combinations(cards,3):
    x = i[0]+i[1]+i[2]
    if max < x and x <= M: max = x 

print(max)
