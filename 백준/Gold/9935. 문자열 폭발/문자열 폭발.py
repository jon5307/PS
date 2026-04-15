from sys import stdin

input = stdin.readline

string = list(input().rstrip())
bomb = list(input().rstrip())
stack = []

for char in string:
    stack.append(char)
    if stack[len(stack) - len(bomb) : len(stack)] == bomb:
        for _ in range(len(bomb)):
            stack.pop()
if stack:
    print(*stack, sep="")
else:
    print("FRULA")
