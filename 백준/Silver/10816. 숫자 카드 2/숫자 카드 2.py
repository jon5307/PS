from collections import deque
import sys
input = sys.stdin.readline

card = {}
input()
for i in map(int, input().split()):
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

input()
for i in map(int,input().split()):
    if i in card:
        print(card[i], end=" ")
    else:
        print("0", end=" ")