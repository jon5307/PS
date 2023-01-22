from sys import stdin, stdout
input = stdin.readline
print = stdout.write

book = {}
n,m = map(int,input().split())
for _ in range(n):
    site, password = input().split()
    book[site] = password

for _ in range(m):
    print(book[input().rstrip()] + '\n')
    