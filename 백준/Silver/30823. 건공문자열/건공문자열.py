from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())
s = input().rstrip()

if k == 1:
    print(s)
elif (n - k) % 2:
    print(s[k - 1 :] + s[: k - 1])
else:
    print(s[k - 1 :] + s[k - 2 :: -1])
