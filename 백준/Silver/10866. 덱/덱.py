from collections import deque
import sys
input = sys.stdin.readline

def push_front(q, x):
    q.appendleft(x)

def push_back(q, x):
    q.append(x)

def pop_front(q):
    if len(q) == 0:
        print(-1)
    else:
        print(q.popleft())
        
def pop_back(q):
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
        elif command == "pop_front\n":
            pop_front(queue)
        elif command == "pop_back\n":
            pop_back(queue)
        else:
            q, x = command.split()
            if q == "push_front":
                push_front(queue, int(x))
            else:
                push_back(queue, int(x))
