from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())
progress = m / n
hour = int(progress * 24)
minute = int((progress * 24 - hour) * 60)
print("%02d:%02d" % (hour, minute))
