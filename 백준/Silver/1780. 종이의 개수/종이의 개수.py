from sys import stdin
input = stdin.readline

def paper(n,y,x,arr,ans):
    num = arr[y][x]
    if not n == 1:
        for i in range(y,y+n):
            for j in range(x,x+n):
                if not arr[i][j] == num:
                    for k in range(y,y+n,n//3):
                        for l in range(x,x+n,n//3):
                            paper(n//3,k,l,arr,ans)
                    return
    ans[num+1] += 1


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

ans = [0,0,0]
paper(n,0,0,arr,ans)
print(*ans,sep="\n")
