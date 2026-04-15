# 입력 받기
n, m = map(int, input().split())

# 학생들의 선호도 입력
preferences = [input().split() for _ in range(n)]

# 질의 입력
queries = [input().split() for _ in range(m)]

# 각 질의에 대해 처리
for query in queries:
    subject, fruit, color = query
    count = 0
    for pref in preferences:
        s, f, c = pref
        if (subject == '-' or subject == s) and \
           (fruit == '-' or fruit == f) and \
           (color == '-' or color == c):
            count += 1
    print(count)
