from math import ceil

p,q = map(int,input().split())
dp = []
for i in range(1,ceil(p**(0.5))):
    if p % i ==0:
        dp.append(i)
        dp.append(p//i)
if int(p**0.5) == p**0.5:
    dp.append(int(p**0.5))
dp.sort()

dq = []
for i in range(1,ceil(q**0.5)):
    if q % i == 0:
        dq.append(i)
        dq.append(q//i)
if int(q**0.5) == q**0.5:
    dq.append(int(q**0.5))
dq.sort()

for a in dp:
    for b in dq:
        print(a,b)