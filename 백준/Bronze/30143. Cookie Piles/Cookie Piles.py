T = int(input())
for _ in range(T):
    N, A, D = map(int, input().split())
    total = N * A + D * N * (N - 1) // 2
    print(total)