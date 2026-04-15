Q = int(input())
for _ in range(Q):
    S = input()
    count = 0
    for i in range(len(S) - 2):
        if S[i] == 'W' and S[i + 1] == 'O' and S[i + 2] == 'W':
            count += 1
    print(count)
