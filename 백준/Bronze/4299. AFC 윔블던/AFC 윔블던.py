S, D = map(int, input().split())

# 두 팀의 점수를 계산
if (S + D) % 2 == 0 and (S - D) % 2 == 0:  
    A = (S + D) // 2
    B = (S - D) // 2
    
    if A >= 0 and B >= 0:  
        print(A, B) if A >= B else print(B, A)
    else:
        print(-1)
else:
    print(-1)