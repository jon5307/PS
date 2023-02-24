from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(1000000)

def check_available(field,y,x,m,n):
    if 0 > x or x >= m or 0 > y or y >= n:
        return False    
    elif not field[y][x]:
        return False
    else:
        return True
    
def worm(field,x,y,m,n):
    field[y][x] = False
    # print("-"*20)
    # print(*field,sep="\n")
    if check_available(field,y,x+1,m,n):
        worm(field,x+1,y,m,n)
    if check_available(field,y,x-1,m,n):
        worm(field,x-1,y,m,n)
    if check_available(field,y+1,x,m,n):
        worm(field,x,y+1,m,n)
    if check_available(field,y-1,x,m,n):
        worm(field,x,y-1,m,n)

def solve():
    m,n,k = map(int,input().split())
    field = [ [False for _ in range(m)] for _ in range(n) ]
    wormcount = 0
    for _ in range(k):
        x,y = map(int,input().split())
        field[y][x] = True
    for i in range(m):
        for j in range(n):
            if field[j][i]:
                worm(field,i,j,m,n)
                wormcount += 1
    print(wormcount)

for _ in range(int(input())):
    solve()