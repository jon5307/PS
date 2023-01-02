from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    bracket = 0
    vps = True
    for i in input().rstrip():
        if i == '(':
            bracket += 1 
        else:
            bracket -= 1
        if bracket < 0:
            vps = False
            break
    if vps and bracket != 0:
        vps = False
    if vps:
        print("YES")
    else:
        print("NO")