N = int(input())
for i in range(N-1):
    print("*" * (i+1), " " * 2 * (N-i-1),"*" * (i+1),sep="")
for i in range(N-1,-1,-1):
    print("*" * (i+1), " " * 2 * (N-i-1),"*" * (i+1),sep="")