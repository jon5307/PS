def can_connect_all_students(N, K, A):
    total_available = sum((a + 1) // 2 for a in A)  # 각 멀티탭에서 사용할 수 있는 콘센트 개수 합산
    return "YES" if total_available >= N else "NO"

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 결과 출력
print(can_connect_all_students(N, K, A))