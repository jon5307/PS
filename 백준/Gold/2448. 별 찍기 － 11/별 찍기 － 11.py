from sys import stdin
from sys import stdout
input = stdin.readline
print = stdout.write

def star_map(star, size, x, y):
    if size == 3:
        star[y][x+2] = True
        star[y+1][x+1] = True
        star[y+1][x+3] = True
        star[y+2][x] = True
        star[y+2][x+1] = True
        star[y+2][x+2] = True
        star[y+2][x+3] = True
        star[y+2][x+4] = True
    else:
        next = size//2
        star_map(star,next,x+next,y)
        star_map(star,next,x,y+next)
        star_map(star,next,x+size,y+next)

N = int(input())
star = [[False for _ in range(2*N-1)] for _ in range(N)]
star_map(star,N,0,0)
for i in range(N):
    for j in range(2*N-1):
        if star[i][j]:
            print("*")
        else:
            print(" ")
    print("\n")
