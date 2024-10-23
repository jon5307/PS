from sys import stdin

input = stdin.readline


class Cog:
    def __init__(self, teeth):
        self.teeth = teeth
        self.top = 0

    def tooth(self, direction):
        if direction == 1:
            return self.teeth[(self.top + 2) % 8]
        elif direction == -1:
            return self.teeth[(self.top - 2) % 8]

    def rotate(self, rotation):
        if rotation == 1:
            self.top = (self.top - 1) % 8
        elif rotation == -1:
            self.top = (self.top + 1) % 8

    def score(self):
        return self.teeth[self.top]


cogs = []

for _ in range(4):
    teeth = []
    for i in input().rstrip():
        teeth.append(int(i))
    cogs.append(Cog(teeth))

for _ in range(int(input())):
    a, direction = map(int, input().rstrip().split())
    a -= 1
    rotate_list = [0] * 4
    rotate_list[a] = direction

    for i in range(a, 3):
        if cogs[i].tooth(1) != cogs[i + 1].tooth(-1):
            rotate_list[i + 1] = -rotate_list[i]
        else:
            break

    for i in range(a, 0, -1):
        if cogs[i].tooth(-1) != cogs[i - 1].tooth(1):
            rotate_list[i - 1] = -rotate_list[i]
        else:
            break

    for i, direction in enumerate(rotate_list):
        cogs[i].rotate(direction)

score = 0
for i, cog in enumerate(cogs):
    score += cog.score() * 2 ** (i)

print(score)
