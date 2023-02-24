from sys import stdin


def com(n, y, x, vid):
    if n == 1:
        print(vid[y][x], end="")
    else:
        first = vid[y][x]
        for i in range(y, y+n):
            for j in range(x, x+n):
                if not first == vid[i][j]:
                    np = n//2
                    print('(', end="")
                    com(np, y, x, vid)
                    com(np, y, x+np, vid)
                    com(np, y+np, x, vid)
                    com(np, y+np, x+np, vid)
                    print(')', end="")
                    return
        print(first, end="")\



n = int(input())
video = []
for _ in range(n):
    video.append(stdin.readline().rstrip())

com(n, 0, 0, video)
