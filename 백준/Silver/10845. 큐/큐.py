from collections import deque
import sys
input = sys.stdin.readline

def push(q, x):
    q.append(x)

def pop(q):
    if len(q) == 0:
        print(-1)
    else:
        print(q.popleft())
        
def rpop(q):
    if len(q) == 0:
        print(-1)
    else:
        print(q.pop())

def size(q):
    print(len(q))

def empty(q):
    if len(q) == 0:
        print(1)
    else:
        print(0)

def front(q):
    if len(q) == 0:
        print(-1)
    else:
        a = q.popleft()
        print(a)
        q.appendleft(a)

def back(q):
    if len(q) == 0:
        print(-1)
    else:
        a = q.pop()
        print(a)
        q.append(a)

if __name__ == "__main__":
    queue = deque()
    for _ in range(int(input())):
        command = input()
        if command == "front\n":
            front(queue)
        elif command == "back\n":
            back(queue)
        elif command == "size\n":
            size(queue)
        elif command == "empty\n":
            empty(queue)
        elif command == "pop\n":
            pop(queue)
        else:
            _, x = command.split()
            push(queue, int(x))
