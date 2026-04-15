import sys

input = sys.stdin.readline

scenario_num = 1  # 시나리오 번호

while True:
    # 적정 체중과 실제 체중 입력
    o, w = map(int, input().split())
    
    if o == 0 and w == 0:  # "0 0" 입력 시 프로그램 종료
        break

    mino = o / 2
    maxo = 2 * o
    is_dead = False  # 펫이 죽었는지 여부

    while True:
        cmd, n = input().split()
        n = int(n)

        if cmd == "#":  # 시나리오 종료
            if is_dead:
                print(scenario_num, "RIP")
            elif mino < w < maxo:
                print(scenario_num, ":-)")
            else:
                print(scenario_num, ":-(")
            
            scenario_num += 1  # 다음 시나리오 번호 증가
            break
        
        if is_dead:  # 펫이 이미 죽었다면 이후 입력 무시
            continue

        if cmd == "F":  # 먹이 주기
            w += n
        elif cmd == "E":  # 운동
            w -= n

        if w <= 0:  # 체중이 0 이하가 되면 사망
            is_dead = True