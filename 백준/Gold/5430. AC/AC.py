from sys import stdin
from collections import deque

input = stdin.readline


def ac(p, n, arr):
    reverse = False
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr[1:-1].split(",")))
    for c in p:
        if c == "R":
            reverse = not reverse
        else:
            if len(arr) == 0:
                print("error")
                return
            if reverse:
                arr.pop()
            else:
                arr.popleft()
    if len(arr) == 0:
        print("[]")
        return
    out = "["
    if reverse:
        while arr:
            out += str(arr.pop()) + ","
    else:
        while arr:
            out += str(arr.popleft()) + ","
    out = out[:-1] + "]"
    print(out)
    return


for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    ac(p, n, arr)
