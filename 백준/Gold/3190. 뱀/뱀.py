from sys import stdin
from collections import deque

input = stdin.readline

di = (-1, 0, 1, 0)  # 상, 우, 하, 좌
dj = (0, 1, 0, -1)

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

# 사과 위치 입력 (0-based index 변환)
for _ in range(k):
    i, j = map(int, input().rstrip().split())
    board[i - 1][j - 1] = 2  # ✅ 1-based index → 0-based index 변환

# 방향 변환 정보 입력
move = {}
l = int(input())
for _ in range(l):
    x, c = input().split()
    move[int(x)] = c

# 초기 설정
snake = deque([(0, 0)])
time = 0
direction = 1  # 처음에는 오른쪽 이동

# 게임 시작
while True:
    time += 1
    i, j = snake[0]
    ni, nj = i + di[direction], j + dj[direction]

    # 벽 또는 자기 자신과 부딪히면 종료
    if ni < 0 or ni >= n or nj < 0 or nj >= n or (ni, nj) in snake:
        break

    # 머리 이동
    snake.appendleft((ni, nj))

    # 사과가 있으면 그대로 (길이 증가), 없으면 꼬리 제거
    if board[ni][nj] == 2:
        board[ni][nj] = 0  # 사과 먹음
    else:
        snake.pop()

    # 방향 변환
    if time in move:
        if move[time] == "L":
            direction = (direction - 1) % 4
        else:  # "D"
            direction = (direction + 1) % 4

print(time)
