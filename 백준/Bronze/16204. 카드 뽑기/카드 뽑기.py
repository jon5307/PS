# 입력 받기
N, M, K = map(int, input().split())

# 앞면과 뒷면이 O인 카드 최대 개수
max_O = min(M, K)

# 앞면과 뒷면이 X인 카드 최대 개수
max_X = min(N - M, N - K)

# 결과 출력
print(max_O + max_X)