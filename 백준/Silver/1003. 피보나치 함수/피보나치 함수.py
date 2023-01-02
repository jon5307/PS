import sys
input = sys.stdin.readline

def fib(n):
    if n == 0:
        print(1,0)
        return
    if n == 1:
        print(0,1)
        return
    list = [0 for _ in range(n+1)]
    list[-1] = 1
    for i in range(n,1,-1):
        list[i-1] += list[i]
        list[i-2] += list[i]
    print(list[0],list[1])


for _ in range(int(input())):
    fib(int(input()))
