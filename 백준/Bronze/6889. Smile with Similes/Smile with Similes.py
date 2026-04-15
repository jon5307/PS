# 입력 받기
n = int(input())
m = int(input())

adjectives = [input() for _ in range(n)]
nouns = [input() for _ in range(m)]

# 모든 조합 출력
for adj in adjectives:
    for noun in nouns:
        print(f"{adj} as {noun}")