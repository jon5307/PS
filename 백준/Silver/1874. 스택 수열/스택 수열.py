from sys import stdin
from collections import deque
input = stdin.readline

def solve(n):
    stack = deque()
    used = [False for _ in range(n)]
    log = ''
    for _ in range(n):
        a = int(input())
        if len(stack) == 0:
            for i in range(1,a):
                if used[i-1] == False:
                    stack.append(i)
                    used[i-1] = True
                    log += '+\n'
            used[a-1] = True
            log += '+\n-\n'
        elif stack[-1] < a:
            for i in range(stack[-1]+1,a):
                if used[i-1] == False:
                    stack.append(i)
                    used[i-1] = True
                    log += '+\n'
            used[a-1] = True
            log += '+\n-\n'
        elif stack[-1] == a:
            stack.pop()
            log += '-\n'
        else:
            print('NO')
            return
    print(log)

solve(int(input()))
