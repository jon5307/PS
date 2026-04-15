def generate_sequence(N):
    sequence = []
    for i in range(1, N + 1):
        if N % 2 == 0:
            # 짝수일 때는 1과 2를 번갈아 사용
            if i % 2 == 1:
                sequence.append(1)
            else:
                sequence.append(2)
        else:
            if i != N:
                # 홀수일 때 마지막을 제외하고는 1과 2를 번갈아 사용
                if i % 2 == 1:
                    sequence.append(1)
                else:
                    sequence.append(2)
            else:
                # 마지막 간선은 3을 사용
                sequence.append(3)
    return sequence

# 입력 받기
N = int(input())

# 수열 생성
result = generate_sequence(N)

# 출력
print(' '.join(map(str, result)))