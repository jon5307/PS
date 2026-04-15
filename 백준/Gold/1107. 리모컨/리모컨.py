from sys import stdin
import itertools

input = stdin.readline

n = int(input())
m = int(input())
button = [True for _ in range(10)]
if m != 0:
    for i in map(int, input().rstrip().split()):
        button[i] = False

possible = ""
for i in range(10):
    if button[i]:
        possible += str(i)

length = len(str(n))
min_press = abs(n - 100)
for i in range(1, length + 2):
    for combo in itertools.product(possible, repeat=i):
        num = int("".join(combo))
        min_press = min(min_press, abs(n - num) + i)

print(min_press)
