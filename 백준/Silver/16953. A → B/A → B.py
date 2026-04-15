from collections import deque

a,b = map(int, input().split())

queue = deque()

queue.append(a)
queue.append(0)
step = 1

while len(queue) > 1:
    c = queue.popleft()
    if c==0:
        step += 1
        queue.append(0)
    else:
        if c == b:
            print(step)
            exit()
        else:
            if c*2 <= b:
                queue.append(c*2)
            if c*10+1 <= b:
                queue.append(c*10+1)

print("-1")

        

