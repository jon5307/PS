while True:
    # 입력 받기
    data = input().strip()
    if data == '0':  # 종료 조건
        break

    N, P = map(int, data.split())

    # 한 장에 인쇄된 페이지 그룹 찾기
    pages = []
    for i in range(1, N + 1, 4):
        sheet = [i, i + 1, N - (i - 1), N - i]
        pages.append(sheet)

    # 선택된 페이지가 포함된 종이 찾기
    for sheet in pages:
        if P in sheet:
            result = sorted([page for page in sheet if page != P])
            print(' '.join(map(str, result)))
            break
