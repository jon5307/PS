from collections import deque

q = deque()
for i in range(1,int(input())+1):
    q.append(i)

a = 0
while True:
    try:
        a = q.popleft()
        a = q.popleft()
        q.append(a)
    except:
        print(a)
        break
