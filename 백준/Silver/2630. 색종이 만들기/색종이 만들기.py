from sys import stdin
input = stdin.readline


def cut_paper(paper,x,y,n,ans):
    blue = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[j][i]:
                blue += 1
    if blue == 0:
        ans[0] += 1
    elif blue == n*n:
        ans[1] += 1
    else:
        nextn = n // 2
        cut_paper(paper,x,y,nextn,ans)
        cut_paper(paper,x+nextn,y,nextn,ans)
        cut_paper(paper,x,y+nextn,nextn,ans)
        cut_paper(paper,x+nextn,y+nextn,nextn,ans)

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(True if i == 1 else False for i in map(int,input().split())))

ans = [0,0]
cut_paper(paper,0,0,n,ans)
print(*ans,sep="\n")
