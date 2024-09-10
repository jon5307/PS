n = input()

for i in range(len(n) - 1, -1, -1):
    if n[i] in ["a", "e", "i", "o", "u"]:
        n = n[0 : i + 1] + "ntry"
        break

print(n)
