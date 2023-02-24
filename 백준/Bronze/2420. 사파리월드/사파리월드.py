from sys import stdin
input = stdin.readline

N, M = map(int,input().split())

print(abs(N-M))