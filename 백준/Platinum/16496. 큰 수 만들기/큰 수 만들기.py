from sys import stdin

input = stdin.readline

n = int(input())
data = input().rstrip().split()
data.sort(key=lambda x: x * 10, reverse=True)
out = "".join(data)
print(int(out))
