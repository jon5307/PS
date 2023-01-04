from sys import stdin
input = stdin.readline

def check_amount(list, size):
    amount = 0
    for i in list:
        amount += i // size
    return amount

K, N = map(int,input().split())

cable = []
for _ in range(K):
    cable.append(int(input()))

left = 0
right = max(cable) + 1

while right - left > 1:
    mid = (left + right) // 2
    amount = check_amount(cable, mid)
    if amount >= N:
        left = mid
    elif amount < N:
        right = mid

if right == left:
    mid = right
else:
    if N == check_amount(cable,right):
        mid = right
    else:
        mid = left

print(mid)
