# 입력 받기
import sys
input = sys.stdin.read
data = input().splitlines()

# 정거장의 수 N과 출발역에서 탑승한 사람의 수 K
N, K = map(int, data[0].split())

# 초기 탑승 인원
current_passengers = K

# 각 정거장 정보 처리
for i in range(1, N + 1):
    A, B = map(int, data[i].split())
    # 하차
    current_passengers -= B
    # 탑승
    current_passengers += A

# 결과 출력
print("비와이")
