list = [0 for _ in range(10001)]
for num in range(1,10000):
    while num < 10000:
        add = 0
        for a in range(len(str(num))):
            add += int(str(num)[a])
        num += add
        if num < 10000:
            list[num] = 1
for i in range(1,10000):
    if list[i] == 0:
        print(i)