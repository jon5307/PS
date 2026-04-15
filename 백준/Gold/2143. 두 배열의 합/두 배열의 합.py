import sys
from collections import Counter

def get_subarray_sums(arr):
    """주어진 배열의 모든 부분 배열 합을 구하는 함수"""
    sub_sums = []
    n = len(arr)
    
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            sub_sums.append(s)
    
    return sub_sums

def count_pairs_with_sum(T, A, B):
    """부분 배열 합을 이용해 T를 만들 수 있는 경우의 수 계산"""
    subA = get_subarray_sums(A)
    subB = get_subarray_sums(B)
    
    # subB의 합 빈도수 계산
    countB = Counter(subB)  

    # T - x를 만족하는 x의 개수 카운팅
    result = 0
    for x in subA:
        target = T - x
        if target in countB:
            result += countB[target]
    
    return result

# 입력 처리
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

# 정답 출력
print(count_pairs_with_sum(T, A, B))
