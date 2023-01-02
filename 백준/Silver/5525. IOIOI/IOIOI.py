import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

check = []
i = 0
con = False
while i + 2 < len(S):
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == "I":
        if con == False:
            check.append(1)
        else:
            check[-1] += 1
        i += 2
        con = True
    else:
        i += 1
        con = False
    
sum = 0
for i in check:
    if i - (N - 1) > 0:
        sum += i - (N - 1)
print(sum)
