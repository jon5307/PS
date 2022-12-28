from math import comb
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int,input().split())
    print(comb(b,a))