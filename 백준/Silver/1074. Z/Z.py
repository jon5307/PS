n,r,c=map(int,input().split())
ans = 0
for i in range(n-1,-1,-1):
    ans <<= 1
    if r & (1 << i):
        ans += 1
    ans <<= 1
    if c & (1 << i):
        ans += 1
print(ans)
