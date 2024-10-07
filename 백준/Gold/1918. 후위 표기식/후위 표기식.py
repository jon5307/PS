from sys import stdin
from collections import deque

input = stdin.readline

exp = input().rstrip()

stack = deque()
ans = []

for e in exp:
    if e in ("+", "-"):
        while stack:
            before = stack.pop()
            if before == "(":
                stack.append(before)
                break
            ans.append(before)
        stack.append(e)
    elif e in ("*", "/"):
        if stack:
            before = stack.pop()
            stack.append(before)
            if before in ("+", "-"):
                stack.append(e)
            elif before in ("*", "/"):
                ans.append(stack.pop())
                stack.append(e)
            else:
                stack.append(e)
        else:
            stack.append(e)
    elif e == "(":
        stack.append("(")
    elif e == ")":
        while stack:
            before = stack.pop()
            if before == "(":
                break
            ans.append(before)
    else:
        ans.append(e)

while stack:
    ans.append(stack.pop())

print(*ans, sep="")
