from sys import stdin
input = stdin.readline

def get_gcd(a:int, b:int) -> int:
    while b != 0:
        a,b = b, a%b
    return a

a,b = map(int, input().split())
if a < b:
    a,b=b,a

gcd = get_gcd(a,b)
print(gcd, a * b // gcd, sep="\n")
