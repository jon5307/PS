from bisect import bisect_left

# 3개 용액 중 합이 0에 가까운 조합을 찾는 함수
def find_three_liquids(n, sol):
    sol.sort()  # 정렬
    min_cv = float("inf")  # 최소 특성값의 절댓값 초기화
    sel_sol = []  # 선택된 세 용액

    for i in range(n - 2):
        start, end = i + 1, n - 1
        while start < end:
            # 현재 세 용액의 합
            s = sol[i] + sol[start] + sol[end]

            # 최소값 갱신
            if abs(s) < abs(min_cv):
                min_cv = s
                sel_sol = [sol[i], sol[start], sol[end]]

            # 합이 0에 가까운 방향으로 포인터 이동
            if s == 0:
                return sel_sol  # 가장 가까운 0이므로 즉시 반환
            elif s > 0:
                end -= 1
            else:
                start += 1

    return sel_sol


# 입력 처리
n = int(input())
sol = list(map(int, input().split()))

# 결과 출력
result = find_three_liquids(n, sol)
print(*result)
