from sys import stdin

input = stdin.readline

a, b = map(int, input().rstrip().split())

valid = [0, 2, 5]
win = [(0, 2), (2, 5), (5, 0)]
if a == b or (not a in valid and not b in valid):
    print("=")
elif (a in valid and not b in valid) or (a, b) in win:
    print(">")
elif (not a in valid and b in valid) or (b, a) in win:
    print("<")
