def count_attacks(time, A, B, C, D):
    cycle1 = A + B
    cycle2 = C + D
    attacks = 0

    if 1 <= (time % cycle1) <= A:
        attacks += 1
    if 1 <= (time % cycle2) <= C:
        attacks += 1

    return attacks

# 입력 받기
A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

# 각 도착 시간에 대한 공격받는 개수 출력
print(count_attacks(P, A, B, C, D))
print(count_attacks(M, A, B, C, D))
print(count_attacks(N, A, B, C, D))