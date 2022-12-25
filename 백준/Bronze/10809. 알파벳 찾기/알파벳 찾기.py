word = input()
alphabet = [-1 for _ in range(26)]
for i in range(len(word)):
    a = ord(word[i]) - 97
    if alphabet[a] == -1:
        alphabet[a] = i
for i in alphabet:
    print(i, end = " ")