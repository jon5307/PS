from sys import stdin


input = stdin.readline


r = input().rstrip()
sum = 0
l = 1
for i in r[::-1]:
    sum += (ord(i) - ord("A") + 1) * l
    l *= 26

print(sum)
