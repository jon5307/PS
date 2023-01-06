a=0
input()
i = 0
for w in input():
    a += (ord(w)-96) * 31**i
    i+=1
print(a % 1234567891)
