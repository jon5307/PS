from sys import stdin

input = stdin.readline


n = int(input())
s = input().rstrip()

if s[-1] == "G":
    print(s[:-1])
else:
    print(s + "G")
