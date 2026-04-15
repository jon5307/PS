l, p = map(int, input().rstrip().split())
person = l * p
for i in map(int, input().rstrip().split()):
    print(i - person, end=" ")