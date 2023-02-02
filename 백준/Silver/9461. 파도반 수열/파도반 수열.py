from sys import stdin
input = stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    if n < 4:
        print(1)
    elif n < 6:
        print(2)
    else:
        queue = [1,1,1,2,2]
        ans = 2
        for _ in range(5,n):
            ans += queue.pop(0)
            queue.append(ans)
        print(ans)
