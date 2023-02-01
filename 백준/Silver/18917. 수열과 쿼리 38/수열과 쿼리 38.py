from sys import stdin
input = stdin.readline


sum = 0
xor = 0
for _ in range(int(input())):
    cmd = list(map(int,input().split()))
    if len(cmd) == 2:
        if cmd[0] == 1:
            sum += cmd[1]
            xor ^= cmd[1]
        else:
            sum -= cmd[1]
            xor ^= cmd[1]
            
    else:
        if cmd[0] == 3:
            print(sum)
        else:
            print(xor)
