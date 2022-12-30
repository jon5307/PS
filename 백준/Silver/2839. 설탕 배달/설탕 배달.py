N = int(input())
bag = N // 5
left = N % 5

while True:
    if left > N:
        bag = -1
        break
    elif left % 3 == 0:
        bag += left // 3
        break
    else:
        left += 5
        bag -= 1

print(bag)