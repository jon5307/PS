from sys import stdin

for _ in range(int(input())):
    l = int(input())
    a = input()
    b = input()
    wb = 0
    bw = 0
    for i in range(l):
        if a[i] != b[i]:
            if a[i] == "W":
                wb += 1
            else:
                bw += 1
    if wb > bw:
        print(wb)
    else:
        print(bw)
