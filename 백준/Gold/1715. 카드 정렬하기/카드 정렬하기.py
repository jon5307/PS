import heapq
from sys import stdin

input = stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)

total_cost = 0

while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    cost = first + second
    total_cost += cost
    heapq.heappush(cards, cost)

# 결과 출력
print(total_cost)
