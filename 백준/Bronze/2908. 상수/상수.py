a,b = input().split(" ")
c = ""
d = ""
for i in a:
    c = i + c
for i in b:
    d = i + d
if int(c) > int(d):
    print(c)
else:
    print(d)