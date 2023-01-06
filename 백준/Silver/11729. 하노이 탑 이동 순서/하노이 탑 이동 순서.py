def move(n,f,t,b):
    if n == 1:
        return f,t
    else:
        return move(n-1,f,b,t) + move(1,f,t,b) + move(n-1,b,t,f)

a = move(int(input()),1,3,2)
print(len(a)//2)
for i in range(0,len(a),2):
    print(a[i],a[i+1])
