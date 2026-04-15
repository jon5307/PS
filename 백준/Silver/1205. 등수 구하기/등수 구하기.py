def find_rank(N, new_score, P, scores):
    if N == 0:  # 현재 랭킹 리스트가 비어있다면
        return 1  # 무조건 1등

    # 1. 태수의 점수가 들어갈 위치 찾기
    rank = 1
    for i in range(N):
        if scores[i] > new_score:
            rank += 1
        elif scores[i] == new_score:
            continue
        else:
            break

    # 2. 랭킹 리스트가 꽉 찼을 때, 마지막 점수보다 작다면 등수에 못 들어감
    if N == P and new_score <= scores[-1]:
        return -1

    return rank

# 입력 받기
N, new_score, P = map(int, input().split())

if N > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

# 결과 출력
print(find_rank(N, new_score, P, scores))