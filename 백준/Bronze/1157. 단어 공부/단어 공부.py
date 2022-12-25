a = input().upper()
list = {}
for i in a:
    try:
        list[i] += 1
    except:
        list[i] = 1
list = sorted(list.items(), key=lambda x:x[1], reverse=True)
try:
    if list[0][1] != list[1][1]:
        print(list[0][0])
    else:
        print("?")
except:
    print(list[0][0])