from sys import stdin

input = stdin.readline

a = input().rstrip()

if a == "M":
    print("MatKor")
elif a == "W":
    print("WiCys")
elif a == "C":
    print("CyKor")
elif a == "A":
    print("AlKor")
elif a == "$":
    print("$clear")
