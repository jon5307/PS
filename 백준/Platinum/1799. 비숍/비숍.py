from sys import stdin

input = stdin.readline

n = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

blocked_rd = set()
blocked_ru = set()


def back_tracking(index, current_bishop, color):
    global max_bishop
    if index >= len(positions[color]):
        max_bishop = max(max_bishop, current_bishop)
        return

    x, y = positions[color][index]
    rd = x + y
    ru = x - y
    if rd not in blocked_rd and ru not in blocked_ru and board[x][y]:
        blocked_rd.add(rd)
        blocked_ru.add(ru)
        back_tracking(index + 1, current_bishop + 1, color)
        blocked_rd.remove(rd)
        blocked_ru.remove(ru)
    back_tracking(index + 1, current_bishop, color)


positions = [[], []]
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            positions[0].append((i, j))
        else:
            positions[1].append((i, j))
max_bishop = 0
back_tracking(0, 0, 0)
white_max_bishop = max_bishop

max_bishop = 0
back_tracking(0, 0, 1)
black_max_bishop = max_bishop

print(white_max_bishop + black_max_bishop)
