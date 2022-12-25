a = input()
list = a.split(" ")
if list[0] == "":
    del list[0]
if list[-1] == "":
    del list[-1]
print(len(list))
