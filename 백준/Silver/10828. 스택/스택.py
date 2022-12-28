from collections import deque
import sys
input = sys.stdin.readline

def push(s, x):
    s.append(x)

def pop(s):
    if len(s) == 0:
        print(-1)
    else:
        print(s.pop())

def size(s):
    print(len(s))

def empty(q):
    if len(q) == 0:
        print(1)
    else:
        print(0)

def top(s):
    if len(s) == 0:
        print(-1)
    else:
        a = s.pop()
        print(a)
        s.append(a)

if __name__ == "__main__":
    stack = deque()
    for _ in range(int(input())):
        command = input()
        if command == "top\n":
            top(stack)
        elif command == "size\n":
            size(stack)
        elif command == "empty\n":
            empty(stack)
        elif command == "pop\n":
            pop(stack)
        else:
            _, x = command.split()
            push(stack, int(x))
