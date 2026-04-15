from sys import stdin

input = stdin.readline

n = int(input())
board = list(map(int, input().rstrip().split()))

dp = [[] for _ in range(n)]
for i in range(n):
    start = i - 1
    end = i + 1
    dp[i].append(True)
    if end >= n:
        continue
    dp[i].append(board[start + 1] == board[end])
    while start >= 0 and end < n:
        if dp[i][-2] == False:
            dp[i].append(False)
        else:
            dp[i].append(board[start] == board[end])
        if (end - start) % 2 == 0:
            end += 1
        else:
            start -= 1

for _ in range(int(input())):
    s, e = map(int, input().rstrip().split())
    print(1 if dp[((s + e) // 2) - 1][e - s] else 0)
