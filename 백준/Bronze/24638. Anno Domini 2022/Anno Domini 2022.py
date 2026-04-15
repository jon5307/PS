from sys import stdin

input = stdin.readline

a, b = input().rstrip().split()
c, d = input().rstrip().split()

if a == "AD" and c == "AD":
    print(abs(int(b) - int(d)))
elif b == "BC" and d == "BC":
    print(abs(int(a) - int(c)))
else:
    print(
        abs(
            int(int(a) if b == "BC" else 1 - int(b))
            - int(int(c) if d == "BC" else 1 - int(d))
        )
    )
