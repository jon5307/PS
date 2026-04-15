# 입력
N, H = map(int, input().split())
ride_heights = list(map(int, input().split()))

# 조건을 만족하는 놀이기구 수 세기
count = sum(1 for height in ride_heights if H >= height)

# 출력
print(count)