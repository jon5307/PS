from sys import stdin

input = stdin.readline

n = int(input())
history = []
for i in range(n):
    word = input().rstrip()
    if word != "?":
        history.append(word)
    else:
        unkonwn_idx = i

if n == 1:
    start = None
    end = None
elif unkonwn_idx == 0:
    start = None
    end = history[0][0]
elif unkonwn_idx == n - 1:
    start = history[-1][-1]
    end = None
else:
    start = history[unkonwn_idx - 1][-1]
    end = history[unkonwn_idx][0]
history = set(history)

m = int(input())
for _ in range(m):
    candidate = input().rstrip()
    if (
        not candidate in history
        and (start == None or start == candidate[0])
        and (end == None or end == candidate[-1])
    ):
        print(candidate)
        exit(0)
