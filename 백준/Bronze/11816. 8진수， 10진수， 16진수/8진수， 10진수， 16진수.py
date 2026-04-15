from sys import stdin

input = stdin.readline


num = input().rstrip()
if num.startswith("0x"):
    print(int(num, 16))
elif num.startswith("0"):
    print(int(num, 8))
else:
    print(int(num))
