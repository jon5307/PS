big = 0
count = 1
for i in range(9):
    num = int(input())
    if big < num:
        big = num
        count = i + 1
print(big)
print(count)
