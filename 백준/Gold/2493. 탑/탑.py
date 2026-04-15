def laser_signals(N, heights):
    result = [0] * N  # 결과를 저장할 리스트
    stack = []  # 스택: (탑의 높이, 탑의 인덱스) 저장
    
    for i in range(N):
        # 현재 탑보다 낮은 탑들은 제거
        while stack and stack[-1][0] <= heights[i]:
            stack.pop()
        
        # 스택이 비어 있지 않다면, 가장 먼저 수신할 수 있는 탑의 번호 저장
        if stack:
            result[i] = stack[-1][1] + 1  # 인덱스는 0부터 시작하므로 +1
        
        # 현재 탑을 스택에 추가
        stack.append((heights[i], i))
    
    return result

# 입력 처리
N = int(input())
heights = list(map(int, input().split()))

# 결과 출력
print(' '.join(map(str, laser_signals(N, heights))))
