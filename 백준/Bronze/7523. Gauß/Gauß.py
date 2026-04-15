def sum_of_integers(n, m):
    return (m - n + 1) * (n + m) // 2

def main():
    t = int(input())  # 테스트 케이스의 개수를 입력받음
    for i in range(1, t + 1):
        n, m = map(int, input().split())  # n과 m을 입력받음
        result = sum_of_integers(n, m)
        print(f"Scenario #{i}:")
        print(result)
        if i != t:
            print()  # 테스트 케이스 사이에 빈 줄 출력

if __name__ == "__main__":
    main()
