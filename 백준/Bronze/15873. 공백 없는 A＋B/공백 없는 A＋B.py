a = input()
if len(a) == 2:
    print(int(a[1]) + int(a[0]))
elif len(a) == 3:
    if a[1] == "0":
        print(int(a[0:2]) + int(a[2]))
    else:
        print(int(a[0]) + int(a[1:3]))
else:
    print(20)
