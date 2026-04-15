K = int(input())

base = "AKARAKA"
overlap_part = "RAKA"  # 마지막 4글자만 붙이면 다음 AKARAKA가 됨

result = base
for _ in range(K - 1):
    result += overlap_part

print(result)