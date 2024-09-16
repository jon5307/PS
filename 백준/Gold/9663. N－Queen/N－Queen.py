from sys import stdin

input = stdin.readline

n = int(input())


def dfs(col: int, filled: list, n: int):
    if col == n:
        return 1

    count = 0
    for i in range(n):
        valid = True
        for j in range(col):
            if i == filled[j] or abs(i - filled[j]) == abs(col - j):
                valid = False
                break
        if valid:
            filled[col] = i
            count += dfs(col + 1, filled, n)
    return count


print(dfs(0, [-1 for _ in range(n)], n))
