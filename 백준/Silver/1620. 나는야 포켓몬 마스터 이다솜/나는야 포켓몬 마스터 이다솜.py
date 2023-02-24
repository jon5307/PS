from sys import stdin, stdout
input = stdin.readline
print = stdout.writelines

n,m = map(int,input().split())
pokedex = ['' for _ in range(n)]
for i in range(n):
    pokedex[i] = input()

for _ in range(m):
    poke = input()
    if poke.rstrip().isdigit():
        print(pokedex[int(poke)-1])
    else:
        print(str(pokedex.index(poke)+1)+'\n')
