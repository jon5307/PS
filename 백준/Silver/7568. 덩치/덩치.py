from sys import stdin
input = stdin.readline

n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))

for p in people:
    rank = 1
    for i in range(n):
        if p[0] < people[i][0] and p[1] < people[i][1]:
            rank += 1
    print(rank, end=' ')
