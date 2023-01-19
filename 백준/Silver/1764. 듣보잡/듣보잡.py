from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
people = {}
for _ in range(n):
    # add 1 to the value of the key
    people[input().rstrip()] = 1

for _ in range(m):
    p = input().rstrip()
    if p in people:
        people[p] += 1
    else:
        people[p] = 1

dbj = [i for i in people if people[i] == 2]

dbj.sort()
print(len(dbj))
print(*dbj,sep='\n')
