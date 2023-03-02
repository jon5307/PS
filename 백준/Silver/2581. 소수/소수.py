from sys import stdin
input = stdin.readline

m = int(input())
n = int(input())
prime = [True for _ in range(n+1)]
prime[1] = False

for i in range(2, n+1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False

sum = 0
for i in range(m, n+1):
    if prime[i]:
        sum += i

if sum == 0:
    print(-1)
    exit()
else:
    print(sum)

for i in range(m, n+1):
    if prime[i]:
        print(i)
        exit()
