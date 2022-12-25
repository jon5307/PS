time = 0
for i in input():
    i = ord(i) - 59
    if 6<=i<24:
        j = i // 3
    else:
        if i == 31:
            j = 9
        else:
            j = (i-1) // 3
    time += j + 1
print(time)
