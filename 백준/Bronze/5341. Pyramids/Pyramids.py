while True:
    a = int(input())
    if a == 0:
        exit(0)
    else:
        if a % 2 == 0:
            print((a+1)*(a//2))
        else:
            print(((a+1)//2)*a)
        