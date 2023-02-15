from sys import stdin

for i in stdin.read().split("\n"):
    if i == "":
        exit()
    n,s = map(int,i.split())
    print(s//(n+1))
