from sys import stdin
input = stdin.readline

grade = input()
score = 0.0
if grade[0] == 'A':
    score += 4
elif grade[0] == 'B':
    score += 3
elif grade[0] == "C":
    score += 2
elif grade[0] == "D":
    score += 1
else:
    print(0.0)
    exit(0)
if grade[1] == "+":
    score += 0.3
elif grade[1] == "-":
    score -= 0.3
print(score)
