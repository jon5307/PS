def move(n,f,t,b):
    if n == 1:
        print(f,t)
    else:
        move(n-1,f,b,t) 
        move(1,f,t,b)
        move(n-1,b,t,f)

n = int(input())
print(2**n-1)
a = move(n,1,3,2)
