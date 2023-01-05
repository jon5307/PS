from sys import stdin
input = stdin.readline

M,N = map(int,input().split())

test = int(N ** 0.5)
prime = [True for _ in range(N)]
prime[0] = False
for i in range(2, test + 1):
    if prime[i - 1] == True: # i is prime
        com = i * 2
        while com <= N:
            prime[com-1] = False
            com += i

for i in range(M-1,N):
    if prime[i] == True:
        print(i+1)
