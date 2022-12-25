while True:
    d = list(map(int, input().split()))
    d.sort()
    if d[0]==0 and d[1]==0 and d[2]==0:
        break
    elif pow(d[0],2) + pow(d[1],2) == pow(d[2],2):
        print("right")
    else:
        print("wrong")