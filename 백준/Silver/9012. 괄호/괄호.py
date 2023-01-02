from sys import stdin
input = stdin.readline

def check(ps: str) -> bool:
    bracket = 0
    for i in ps:
        if i == '(':
            bracket += 1 
        else:
            bracket -= 1
        if bracket < 0:
            return False
    if bracket != 0:
        return False
    else:
        return True

for _ in range(int(input())):
    bracket = 0
    vps = True
    if check(input().rstrip()):
        print("YES")
    else:
        print("NO")
