for _ in range(int(input())):
    a, b = input().split(" ")
    for i in range(len(b)):
        print(b[i] * int(a), end = "")
    print()