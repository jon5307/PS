import sys
input = sys.stdin.readline

N = int(input())
num = tuple(map(int,input().split()))

# make prime list
max = max(num)
test = int(max ** 0.5)
prime = [True for _ in range(max)]
prime[0] = False
for i in range(2, test + 1):
    if prime[i - 1] == True: # i is prime
        com = i * 2
        while com <= max:
            prime[com-1] = False
            com += i

sum = 0
for check in num:
    if prime[check-1]:
        sum+=1

print(sum)
