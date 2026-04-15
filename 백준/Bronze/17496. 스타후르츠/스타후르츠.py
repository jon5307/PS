# 입력 받기
N, T, C, P = map(int, input().split())

# 스타후르츠를 심을 수 있는 날짜 범위 계산
# 첫 번째 날부터 시작하여 T일 단위로 심을 수 있음
harvest_days = (N - 1) // T  # T일 단위로 수확 가능한 횟수

# 총 수익 계산
total_fruits = harvest_days * C  # 총 수확 가능한 스타후르츠 개수
total_profit = total_fruits * P  # 총 수익

# 결과 출력
print(total_profit)