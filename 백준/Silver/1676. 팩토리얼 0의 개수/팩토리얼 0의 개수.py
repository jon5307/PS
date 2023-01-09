from sys import stdin
input = stdin.readline

sum = 1
for i in range(1,int(input())+1):
    sum = i * sum

zeros = 0
while True:
    if sum % 10**zeros == 0:
        zeros += 1
    else:
        break

print(zeros-1)
