from sys import stdin

input = stdin.readline


def is_consonant(char):
    """Check if a character is a consonant."""
    return char not in "aeiouy"


while True:
    word = input().rstrip()
    if word == "quit!":
        break
    if len(word) > 4 and word[-2:] == "or" and is_consonant(word[-3]):
        print(word[:-2] + "our")
    else:
        print(word)
