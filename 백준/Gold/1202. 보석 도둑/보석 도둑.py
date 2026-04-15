from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

# 입력 처리
n, k = map(int, input().split())
gems = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    heappush(gems, (m, v))  # 무게 기준으로 최소 힙에 삽입

for _ in range(k):
    heappush(bags, int(input()))  # 가방 무게를 최소 힙에 삽입

# 알고리즘
total_value = 0
available_gems = []

while bags:
    bag_capacity = heappop(bags)  # 가장 작은 가방부터 처리
    
    # 가방에 넣을 수 있는 보석들을 `available_gems`에 추가
    while gems and gems[0][0] <= bag_capacity:
        m, v = heappop(gems)
        heappush(available_gems, -v)  # 보석의 가치를 최대 힙으로 저장
    
    # 가장 가치가 큰 보석을 선택
    if available_gems:
        total_value += -heappop(available_gems)

print(total_value)
