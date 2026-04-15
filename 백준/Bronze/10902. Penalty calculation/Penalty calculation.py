n = int(input())
submissions = []

for _ in range(n):
    t, s = map(int, input().split())
    submissions.append((t, s))

# 가장 높은 점수 구하기
max_score = max(s for _, s in submissions)

# 그 점수를 처음으로 받은 제출 찾기 (가장 작은 번호 f)
for i, (t, s) in enumerate(submissions):
    if s == max_score:
        f = i + 1  # 제출 번호는 1-based
        tf = t
        sf = s
        break

# 페널티 계산
if sf == 0:
    print(0)
else:
    print(tf + (f - 1) * 20)
