from sys import stdin

input = stdin.readline
NOT_CLEANED = 0
WALL = 1
CLEANED = 2

n, m = map(int, input().rstrip().split())

r, c, d = map(int, input().rstrip().split())

room = [list(map(int, input().rstrip().split())) for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

clean_count = 0

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[r][c] == NOT_CLEANED:
        room[r][c] = CLEANED
        clean_count += 1
    go = False
    for i in range(d - 1, d - 5, -1):
        if room[r + direction[i % 4][0]][c + direction[i % 4][1]] == NOT_CLEANED:
            r += direction[i % 4][0]
            c += direction[i % 4][1]
            d = i % 4
            go = True
            break
    if not go:
        if room[r - direction[i % 4][0]][c - direction[i % 4][1]] != WALL:
            r -= direction[i % 4][0]
            c -= direction[i % 4][1]
        else:
            break

print(clean_count)
