n = int(input())
move = 1
position = 1
multiplier = 0
while n > position:
    move += 1
    multiplier += 1
    position += 6 * multiplier
print(move)