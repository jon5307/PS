from sys import stdin

input = stdin.readline

s = input().rstrip()
i = 0
while i < len(s):
    if s[i : i + 2] == "pi":
        i += 2
    elif s[i : i + 2] == "ka":
        i += 2
    elif s[i : i + 3] == "chu":
        i += 3
    else:
        print("NO")
        exit(0)
print("YES")
