total = int(input())
cash = 0
for _ in range(int(input())):
    price, amount = map(int,input().split())
    cash += price * amount
if total == cash:
    print("Yes")
else:
    print("No")