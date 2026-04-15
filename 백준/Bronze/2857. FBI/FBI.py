# 5개의 첩보원명을 입력받습니다.
agents = [input().strip() for _ in range(5)]

# FBI가 포함된 첩보원의 인덱스를 저장할 리스트
fbi_agents = []

# 각 첩보원명에 "FBI"가 포함되어 있는지 확인
for idx, name in enumerate(agents, 1):  # 1부터 시작하는 인덱스
    if "FBI" in name:
        fbi_agents.append(str(idx))  # 문자열로 변환하여 저장

# 결과 출력
if fbi_agents:
    print(' '.join(fbi_agents))
else:
    print("HE GOT AWAY!")