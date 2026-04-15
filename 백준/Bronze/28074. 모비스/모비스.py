input_string = input()
if all(c in input_string for c in ("M", "O", "B", "I", "S")):
    print("YES")
else:
    print("NO")