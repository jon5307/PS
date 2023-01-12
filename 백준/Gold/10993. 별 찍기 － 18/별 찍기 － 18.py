from sys import stdin
input = stdin.readline
# from sys import stdout
# print = stdout.write

def star_make(star, size, x, y):
    if size == 1:
        star[y][x] = '*'
    else:
        x_end = 2**(size+1)-4
        y_end = 2**size-2
        if size % 2 == 0: # reverse triangle
            for i in range(x_end):
                star[y][x+i] = '*'
            for i in range(y_end):
                star[y+i][x+x_end-i] = '*'
            for i in range(1,y_end+1):
                star[y+i][x+i] = '*'
            star_make(star,size-1,x+x_end//4+1,y+1)
        else: # normal triangel
            for i in range(x_end):
                star[y+y_end][x+i] = '*'
            for i in range(y_end):
                star[y+y_end-i][x+x_end-i] = '*'
            for i in range(1,y_end+1):
                star[y+y_end-i][x+i] = '*'
            star_make(star,size-1,x+x_end//4+1,y+y_end//2)

N = int(input())
x = 2**(N+1)-3
y = 2**N-1
if N % 2 == 0:
    star = [[" " for _ in range(x-i)] for i in range(y)]
else:
    star = [[" " for _ in range((x+1)//2+i)] for i in range(y)]

star_make(star,N,0,0)
for i in star:
    print(*i,sep="")
