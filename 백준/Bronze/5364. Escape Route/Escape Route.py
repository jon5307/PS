import math

# 입력 받기
n = int(input())  # 총 좌표의 개수
coordinates = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# 현재 위치
current_location = coordinates[0]
current_x, current_y = current_location

# 가장 가까운 행성 찾기
min_distance = float('inf')
closest_planet = None

for i in range(1, n):
    planet_x, planet_y = coordinates[i]
    
    # 두 점 사이의 거리 계산
    distance = math.sqrt((current_x - planet_x) ** 2 + (current_y - planet_y) ** 2)
    
    # 가장 가까운 행성 업데이트
    if distance < min_distance:
        min_distance = distance
        closest_planet = (planet_x, planet_y)

# 결과 출력
print(f"{current_x} {current_y}")
print(f"{closest_planet[0]} {closest_planet[1]}")
print(f"{min_distance:.2f}")
