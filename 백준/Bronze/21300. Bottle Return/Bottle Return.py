def calculate_refund(containers):
    deposit_per_container = 5  # 5 cents per container
    total_refund = sum(containers) * deposit_per_container
    return total_refund

# 입력 받기
containers = list(map(int, input().split()))

# 환불 금액 계산 및 출력
print(calculate_refund(containers))
