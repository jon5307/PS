seek = input()

s = 0
sum = 0
sub_all = False
for i in range(len(seek)):
    if seek[i] == "-" or seek[i] == "+":
        if s == 0:
            sum += int(seek[s:i])
        elif sub_all or seek[s - 1] == "-":
            sum -= int(seek[s:i])
            sub_all = True
        else:
            sum += int(seek[s:i])
        s = i + 1
    elif len(seek) == i + 1:
        if sub_all or seek[s - 1] == "-":
            sum -= int(seek[s : i + 1])
            sub_all = True
        else:
            sum += int(seek[s : i + 1])
        s = i + 1


print(sum)
