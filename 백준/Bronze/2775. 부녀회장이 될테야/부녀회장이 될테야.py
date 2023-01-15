from sys import stdin
input = stdin.readline

def solve():
    k = int(input()) + 1
    n = int(input())
    apt = [[i for i in range(1,n+1)]] + [ [0 for _ in range(n)] for _ in range(k-1)]
    for i in range(1,k):
        apt[i][0] = 1
    for i in range(1,k):
        for j in range(1,n):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]
    print(apt[k-1][n-1])

for _ in range(int(input())):
    solve()
    