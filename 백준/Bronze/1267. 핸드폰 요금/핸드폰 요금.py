def calculate_costs(N, call_times):
    Y_total = 0
    M_total = 0
    for time in call_times:
        # 영식 요금제 계산
        Y_cost = ((time // 30) + 1) * 10
        Y_total += Y_cost
        
        # 민식 요금제 계산
        M_cost = ((time // 60) + 1) * 15
        M_total += M_cost
        
    if Y_total < M_total:
        print(f"Y {Y_total}")
    elif M_total < Y_total:
        print(f"M {M_total}")
    else:
        print(f"Y M {Y_total}")

# 입력 받기
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    call_times = list(map(int, data[1:N+1]))
    calculate_costs(N, call_times)

if __name__ == "__main__":
    main()
