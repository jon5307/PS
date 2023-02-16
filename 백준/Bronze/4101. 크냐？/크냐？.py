from sys import stdin

for i in stdin.read().split("\n"):
    a,b = map(int,i.split())
    if a == 0 and b == 0:
        exit(0)
    elif a > b:
        print("Yes")
    else:
        print("No")
