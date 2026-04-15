n = int(input())  # 캐릭터 수
gahui_votes = int(input())  # 가희가 지지하는 캐릭터의 투표 수
other_votes = list(map(int, input().split()))  # 나머지 캐릭터들의 투표 수

higher_count = sum(1 for v in other_votes if v > gahui_votes)
print(higher_count + 1)