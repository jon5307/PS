# 입력받기
n = int(input())  # 데이터 세트 수
results = []  # 결과 저장 리스트

for _ in range(n):
    dataset = list(map(int, input().split()))  # 각 데이터 세트
    results.append(dataset)

# 출력 및 결과 처리
for dataset in results:
    print(" ".join(map(str, dataset)))  # 데이터 세트 출력

    mack = 18 in dataset
    zack = 17 in dataset

    if mack and zack:
        print("both")
    elif mack:
        print("mack")
    elif zack:
        print("zack")
    else:
        print("none")

    print()  # 각 데이터 세트 후 빈 줄 출력