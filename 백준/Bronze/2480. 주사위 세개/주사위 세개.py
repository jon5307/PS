a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a != b != c != a:
    print(max(a,b,c)*100)
else:
    if a == b:
        print(a * 100 + 1000)
    elif b == c:
        print(b * 100 + 1000)
    else:
        print(c * 100 + 1000)