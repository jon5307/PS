from sys import stdin

input = stdin.readline

for t in range(int(input())):
    n = int(input())
    if n == 0:
        print(f"Case #{t+1}: INSOMNIA")
    else:
        used = set()
        nn = n
        while True:
            for i in str(nn):
                used.add(int(i))
            if len(used) == 10:
                print(f"Case #{t+1}: {nn}")
                break
            nn += n
