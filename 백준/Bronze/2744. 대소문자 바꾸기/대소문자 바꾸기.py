from sys import stdin
input = stdin.readline

for i in input().rstrip():
    if i.isupper():
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")
        