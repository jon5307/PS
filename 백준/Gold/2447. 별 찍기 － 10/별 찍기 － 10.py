from sys import stdin
input = stdin.readline

def star_map(star, size, x, y):
    if size == 3:
        for i in range(x,x+3):
            for j in range(y,y+3):
                if not (i == x+1 and j == y+1):
                    star[i][j] = True
    else:
        step = size//3
        for i in range(x,x+size,step):
            for j in range(y,y+size,step):
                if not (i == x+step and j == y+step):
                    star_map(star,size//3,i,j)
    return star

N = int(input())
star = [[False for _ in range(N)] for _ in range(N)]
star_map(star,N,0,0)
for i in range(N):
    for j in range(N):
        if star[i][j]:
            print("*",end="")
        else:
            print(" ",end="")
    print()
