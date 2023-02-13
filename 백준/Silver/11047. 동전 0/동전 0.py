from sys import stdin
input = stdin.readline


def coin_zero(coin,ord,amount):
    if amount == 0:
        return 0
    elif len(coin) - 1 == ord:
        return amount // coin[ord]
    else:
        return coin_zero(coin,ord+1,amount%coin[ord]) + amount//coin[ord]

n,k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

print(coin_zero(coin,0,k))
