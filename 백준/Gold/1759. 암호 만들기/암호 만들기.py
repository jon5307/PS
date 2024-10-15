from sys import stdin

input = stdin.readline

l, c = map(int, input().rstrip().split())

v = ("a", "e", "i", "o", "u")

char = list(input().rstrip().split())

char.sort()


def dfs(start, vowel, consonant, seq):
    if len(seq) == l:
        if vowel >= 1 and consonant >= 2:
            print(*seq, sep="")
    else:
        for i in range(start, c):
            if char[i] in v:
                dfs(i + 1, vowel + 1, consonant, seq + [char[i]])
            else:
                dfs(i + 1, vowel, consonant + 1, seq + [char[i]])


dfs(0, 0, 0, [])
