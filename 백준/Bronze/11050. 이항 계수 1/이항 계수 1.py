import sys
input = sys.stdin.readline

def c(a:int,b:int) -> int:
    def loop(a,b):
        if a == b:
            return 1
        elif b == 1:
            return a
        else:
            return loop(a-1,b-1) + loop(a-1,b)
    if a-b > b:
        return loop(a,a-b)
    else:
        return loop(a,b)

a, b = map(int,input().split())
print(c(a,b))