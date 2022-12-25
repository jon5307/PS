word = input()
while(word != "0"):
    is_pal = 1
    for i in range(len(word) // 2 + 1):
        if word[i] != word[-i - 1]:
            is_pal = 0
            break
    if is_pal == 0:
        print("no")
    else:
        print("yes")
    word = input()