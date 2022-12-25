gWordCount = 0
for _ in range(int(input())): #단어
    checkWord = input()
    wordLength = len(checkWord)
    groupWord = True
    for i in range(wordLength): #글자
        fullWord = False
        checkAlphtbet = checkWord[i]
        currentWord = checkAlphtbet
        while checkAlphtbet == currentWord:
            i += 1
            if i == wordLength:
                fullWord = True
                break
            currentWord = checkWord[i]
        if fullWord == True: 
            break
        for j in range(i+1,wordLength):
            if checkAlphtbet == checkWord[j]:
                groupWord = False
                break
    if groupWord == True:
        gWordCount += 1
print(gWordCount)