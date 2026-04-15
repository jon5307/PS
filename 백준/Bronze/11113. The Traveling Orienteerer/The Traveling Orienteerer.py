import sys
import math

input = sys.stdin.read

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    data = input().splitlines()
    n = int(data[0])  # 제어 포인트 개수
    
    # 제어 포인트 좌표 저장
    points = []
    for i in range(1, n + 1):
        x, y = map(float, data[i].split())
        points.append((x, y))
    
    m = int(data[n + 1])  # 경로의 수
    index = n + 2
    results = []

    # 각 경로 계산
    for _ in range(m):
        p = int(data[index])  # 경로 내 포인트 수
        index += 1
        route_indices = list(map(int, data[index].split()))
        index += 1
        
        # 경로의 총 거리 계산
        total_distance = 0
        for j in range(1, p):
            x1, y1 = points[route_indices[j - 1]]
            x2, y2 = points[route_indices[j]]
            total_distance += calculate_distance(x1, y1, x2, y2)
        
        # 결과 저장
        results.append(round(total_distance))

    # 출력
    for result in results:
        print(result)

main()