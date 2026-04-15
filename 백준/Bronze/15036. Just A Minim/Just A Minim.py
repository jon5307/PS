# 입력
N = int(input())
codes = list(map(int, input().split()))

# 코드 -> 노트 수 매핑
note_lengths = {
    0: 2.0,
    1: 1.0,
    2: 0.5,
    4: 0.25,
    8: 0.125,
    16: 0.0625
}

# 전체 길이 계산
total_length = sum(note_lengths[code] for code in codes)

# 출력 (정확도 고려하여 소수점 충분히 출력)
print(f"{total_length:.10f}")
