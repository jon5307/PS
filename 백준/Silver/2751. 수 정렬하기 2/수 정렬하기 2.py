from sys import stdin
input = stdin.readline

list = []
for _ in range(int(input())):
    list.append(int(input()))

list.sort()

for i in list:
    print(i)