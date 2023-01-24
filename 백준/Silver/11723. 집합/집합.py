from sys import stdin
input = stdin.readline

s = [0 for _ in range(20)]

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'add':
        s[int(cmd[-1])-1] = 1
    elif cmd[0] == 'remove':
        s[int(cmd[-1])-1] = 0
    elif cmd[0] == 'check':
        print(s[int(cmd[-1])-1])
    elif cmd[0] == 'toggle':
        if s[int(cmd[-1])-1] == 1:
            s[int(cmd[-1])-1] = 0
        else:
            s[int(cmd[-1])-1] = 1
    elif cmd[0] == 'all':
        s = [1 for _ in range(20)]
    else:
        s = [0 for _ in range(20)]
