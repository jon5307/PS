from math import gcd

# 입력 받기
first_dice = list(map(int, input().split()))
second_dice = list(map(int, input().split()))

# 첫 번째 플레이어가 이기는 경우의 수 계산
win_count = 0
for a in first_dice:
    for b in second_dice:
        if a > b:
            win_count += 1

# 전체 경우의 수는 36
total_count = 6 * 6

# 기약분수로 변환
common_divisor = gcd(win_count, total_count)
numerator = win_count // common_divisor
denominator = total_count // common_divisor

# 결과 출력
print(f"{numerator}/{denominator}")