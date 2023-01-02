from sys import stdin
input = stdin.readline

size = int(input())
list = [0 for _ in range(size)]
for i in range(size):
    list[i] = int(input())

list.sort()

for i in list:
    print(i)