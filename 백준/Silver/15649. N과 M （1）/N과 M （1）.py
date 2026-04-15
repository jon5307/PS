from sys import stdin

input = stdin.readline

def bt(l):
    if l == m:
        print(" ".join(map(str, result)))
    else:
        for i in range(1, n + 1):
            if not used[i]:
                result.append(i)
                used[i] = True
                bt(l + 1)
                used[i] = False
                result.pop()

n, m = map(int, input().rstrip().split())

used = [False] * (n + 1)
result = []
bt(0)
