from sys import stdin
from collections import deque

input = stdin.readline

s = input().rstrip()
mul = 1
ans = 0
stack = deque()

for idx, h in enumerate(s):
    if h in ("(","["):
        stack.append(h)
        mul *= 2 if h == "(" else 3
    elif h == ")":
        if len(stack) == 0 or stack[-1] == "[":
            stack.append(0)
            break
        stack.pop()
        if s[idx-1] == "(":
            ans += mul
        mul //= 2
    elif h == "]":
        if len(stack) == 0 or stack[-1] == "(":
            stack.append(0)
            break
        stack.pop()
        if s[idx-1] == "[":
            ans += mul
        mul //= 3
        
print(ans if len(stack) == 0 else 0)