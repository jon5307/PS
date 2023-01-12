from sys import stdin
input = stdin.readline
from sys import stdout
print = stdout.write

N = int(input())
for i in range(N):
    print(" " * (N-i-1) + "*" * (i+1) + '\n')
for i in range(N-2,-1,-1):
    print(" " * (N-i-1) + "*" * (i+1) + '\n')
    