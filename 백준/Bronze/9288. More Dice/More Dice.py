def find_dice_combinations(case_number, target_sum):
    print(f"Case {case_number}:")
    found = False
    for a in range(1, 7):  # 첫 번째 주사위 값
        b = target_sum - a  # 두 번째 주사위 값
        if a <= b <= 6:  # 유효한 주사위 값인지 확인
            print(f"({a},{b})")
            found = True
    if not found:
        print()  # 가능한 조합이 없는 경우 빈 줄 출력

# 입력 처리
T = int(input())  # 테스트 케이스 개수
for case_num in range(1, T + 1):
    S = int(input())  # 주어진 합
    find_dice_combinations(case_num, S)