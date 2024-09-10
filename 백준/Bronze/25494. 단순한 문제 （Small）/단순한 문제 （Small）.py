from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    amount = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                i = x % y
                j = y % z
                k = z % x
                if i == j and j == k:
                    amount += 1
    print(amount)
