import sys

# 입력 받기
A, B, C = map(int, sys.stdin.readline().split())  # 기술 난이도
N = int(sys.stdin.readline())  # 동아리 수

max_score = 0  # 최고 점수 저장 변수

# 각 동아리별 점수 계산
for _ in range(N):
    team_score = 0
    for _ in range(3):  # 동아리원 3명
        a, b, c = map(int, sys.stdin.readline().split())  # 각 기술 사용 횟수
        team_score += (a * A) + (b * B) + (c * C)  # 개별 점수 합산
    max_score = max(max_score, team_score)  # 최고 점수 갱신

# 결과 출력
print(max_score)