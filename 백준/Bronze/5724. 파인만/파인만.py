while True:
    a = int(input())
    if a == 0:
        break
    s = 0
    for i in range(1, a + 1):
        s += i**2
    print(s)
