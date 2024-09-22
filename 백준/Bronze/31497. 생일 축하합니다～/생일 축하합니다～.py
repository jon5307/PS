from sys import stdin, stdout

input = stdin.readline

n = int(input())
name = [input().rstrip() for _ in range(n)]

for i in name:
    print("? " + i, flush=True)
    a = int(input())
    print("? " + i, flush=True)
    b = int(input())
    if a != b:
        print("! " + i, flush=True)
        break
