from sys import stdin

input = stdin.readline

for i in range(int(input())):
    a = input().rstrip()
    if a[-1] in ("y", "Y"):
        print(f"Case #{i+1}: {a} is ruled by nobody.")
    elif a[-1] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        print(f"Case #{i+1}: {a} is ruled by a queen.")
    else:
        print(f"Case #{i+1}: {a} is ruled by a king.")
