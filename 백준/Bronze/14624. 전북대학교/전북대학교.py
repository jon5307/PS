def print_cbnu_symbol(N):
    if N % 2 == 0:
        print("I LOVE CBNU")
    else:
        # 첫 번째 줄: N개의 '*'
        print('*' * N)
        # 다음 줄들: 중앙을 기준으로 '*'을 배치
        half = (N - 1) // 2
        for i in range(1, half + 2):
            leading_spaces = half - (i - 1)
            if i == 1:
                # 중앙에 '*' 하나
                line = ' ' * leading_spaces + '*'
            else:
                # '*' 두 개, 사이에 공백
                inner_spaces = 2 * (i - 1) - 1
                line = ' ' * leading_spaces + '*' + ' ' * inner_spaces + '*'
            print(line)

# 입력 받기
N = int(input())
print_cbnu_symbol(N)
