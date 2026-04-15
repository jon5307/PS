from sys import stdin

input = stdin.readline

input()
hole = 0
jjak = 0
for i in input().rstrip():
    if int(i) % 2 == 0:
        jjak += 1
    else:
        hole += 1
if jjak > hole:
    print(0)
elif hole > jjak:
    print(1)
else:
    print(-1)
