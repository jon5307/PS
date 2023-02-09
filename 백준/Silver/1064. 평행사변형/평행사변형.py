from sys import stdin
input = stdin.readline
from math import sqrt


vt = list(map(int, input().split()))

hp = []

if (vt[0] - vt[2]) * (vt[3] - vt[5]) == (vt[2] - vt[4]) * (vt[1] - vt[3]):
    print(-1.0)
    exit(0)

for i in range(3):
    hp.append(sqrt(pow(vt[(2*i)%6] - vt[(2*i+2)%6],2) + 
                      pow(vt[(2*i+1)%6] - vt[(2*i+3)%6],2)))

hp.sort()

max_round = 2*(hp[2]+hp[1])
min_round = 2*(hp[1]+hp[0])

print(max_round-min_round)
