from sys import stdin
input = stdin.readline


n,m = map(int,input().split())
fr = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    fr[a-1][b-1] = True
    fr[b-1][a-1] = True

for i in range(n):
    queue = [i,-1]
    connected = [False for _ in range(n)]
    step = 1
    kb_sum = 0
    while len(queue) != 1:
        p = queue.pop(0)
        if p == -1:
            step += 1
            queue.append(-1)
        else:
            for j in range(n):
                if j != i and fr[p][j] and not connected[j]:
                    queue.append(j)
                    connected[j] = True
                    kb_sum += step
    if i == 0:
        kb_min = kb_sum
        min_person = 0
    elif kb_min > kb_sum:
        kb_min = kb_sum
        min_person = i

print(min_person+1)
