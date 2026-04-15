import sys
import bisect

# 1. 완전 세제곱수 리스트 미리 생성 (1³ ~ 1259³)
MAX_N = 2000000000
cubes = []
i = 1
while (i ** 3) <= MAX_N:
    cubes.append(i ** 3)
    i += 1

# 2. 입력 처리
def count_cubes_in_range(A, B):
    """A와 B 사이의 완전 세제곱수 개수를 반환"""
    left = bisect.bisect_left(cubes, A)
    right = bisect.bisect_right(cubes, B)
    return right - left

def main():
    # 입력을 빠르게 읽기
    input_data = sys.stdin.read().splitlines()
    T = int(input_data[0])
    
    results = []
    for case_num in range(1, T + 1):
        A, B = map(int, input_data[case_num].split())
        count = count_cubes_in_range(A, B)
        results.append(f"Case #{case_num}: {count}")
    
    # 출력 최적화 (한 번에 출력)
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()