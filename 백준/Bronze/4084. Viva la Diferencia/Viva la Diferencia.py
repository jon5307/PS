from sys import stdin

input = stdin.readline

while True:
    a, b, c, d = map(int, input().rstrip().split())
    if a == b == c == d == 0:
        break
    seq = 0
    while not a == b == c == d:
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        seq += 1
    print(seq)
