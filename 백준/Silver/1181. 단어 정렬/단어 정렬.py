list = [[]for _ in range(51)]

for _ in range(int(input())):
    word = input()
    if not word in list[len(word)]:
        list[len(word)].append(word)

for i in list:
    i.sort()
    for j in i:
        print(j)
