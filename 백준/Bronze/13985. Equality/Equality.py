from sys import stdin

input = stdin.readline


a, _, b, _, c = input().split()
if int(a) + int(b) == int(c):
    print("YES")
else:
    print("NO")
