n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(n):
    c+= a[i]-b[i] if a[i]-b[i] >0 else 0
print(c)