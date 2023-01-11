from sys import stdin
input = stdin.readline

def check_balance(sentence):
    bracket = []
    for word in sentence:
        if word == "(":
            bracket.append('(')
        elif word == '[':
            bracket.append('[')
        elif word == ')':
            if len(bracket) == 0 or bracket[-1] == '[':
                return False
            else:
                bracket.pop()
        elif word == ']':
            if len(bracket) == 0 or bracket[-1] == '(':
                return False
            else:
                bracket.pop()
    if len(bracket) == 0:
        return True
    else:
        return False
    

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break
    if check_balance(sentence):
        print('yes')
    else:
        print('no')
        