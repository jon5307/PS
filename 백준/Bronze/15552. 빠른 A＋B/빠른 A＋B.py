import sys
x = int(sys.stdin.readline().rstrip())
for _ in range(x):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)