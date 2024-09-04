def bfs(N, M, l):
    if len(l) == M:
        print(*l, sep=" ")
        return
    if len(l) == 0:
        for i in range(1, N + 1):
            bfs(N, M, [i])
        return
    if l[-1] > N:
        return
    for i in range(l[-1], N + 1):
        bfs(N, M, l + [i])


if __name__ == "__main__":
    N, M = map(int, input().split())
    bfs(N, M, [])
