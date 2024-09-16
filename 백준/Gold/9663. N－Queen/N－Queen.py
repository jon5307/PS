from sys import stdin

input = stdin.readline

n = int(input())


def dfs(col: int, filled: list, n: int):
    sum = 0
    if col == n - 1:
        for i in range(n):
            use = True
            for j in range(len(filled)):
                if (
                    i == filled[j]
                    or i - filled[j] == j - col
                    or i - filled[j] == col - j
                ):
                    use = False
                    break
            if use:
                sum += 1
        return sum
    elif col == 0:
        for i in range(n):
            sum += dfs(col + 1, filled + [i], n)
        return sum
    else:
        for i in range(n):
            use = True
            for j in range(len(filled)):
                if (
                    i == filled[j]
                    or i - filled[j] == j - col
                    or i - filled[j] == col - j
                ):
                    use = False
                    break
            if use:
                sum += dfs(col + 1, filled + [i], n)
        return sum


print(dfs(0, [], n))
