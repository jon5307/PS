n, k = map(int, input().split())
games = [list(map(int, input().split())) for _ in range(n)]

games.sort(key=lambda x: (x[1], x[0]))
games.sort(key=lambda x: ((x[2] * 10**9) // x[1]), reverse=True)
for i in range(k):
    print(games[i][0])
