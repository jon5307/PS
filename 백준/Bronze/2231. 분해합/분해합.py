N = int(input())
a = 0
test = 0
while test != N and a < N:
    a += 1
    test = a
    for i in str(a):
        test += int(i)

if a == N:
    print(0)
else:
    print(a)
