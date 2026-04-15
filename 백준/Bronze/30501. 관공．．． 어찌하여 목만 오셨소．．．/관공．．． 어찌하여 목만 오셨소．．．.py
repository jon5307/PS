# 용의자 수 입력
N = int(input().strip())

# 용의자 이름 리스트 생성 및 검색
for _ in range(N):
    name = input().strip()
    if 'S' in name:
        print(name)
        break