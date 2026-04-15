from sys import stdin

input = stdin.readline


def palindrome(word, pal):
    s = 0
    e = len(word) - 1
    while e - s > 0:
        if word[s] != word[e]:
            if pal == 0:
                if word[s + 1] == word[e] and word[s] == word[e - 1]:
                    return min(
                        palindrome(word[s + 1 : e + 1], 1), palindrome(word[s:e], 1)
                    )
                if word[s + 1] == word[e]:
                    s += 1
                    pal = 1
                elif word[s] == word[e - 1]:
                    e -= 1
                    pal = 1
                else:
                    return 2
            else:
                return 2
        s += 1
        e -= 1
    return pal


for _ in range(int(input())):
    s = input().rstrip()
    print(palindrome(s, 0))
