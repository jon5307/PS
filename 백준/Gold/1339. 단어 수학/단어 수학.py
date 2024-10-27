from sys import stdin

input = stdin.readline

n = int(input())

char_count = {}
for _ in range(n):
    for i, char in enumerate(input().rstrip()[::-1]):
        char_count[char] = char_count.get(char, 0) + 10**i

count_list = list(char_count.values())
count_list.sort(reverse=True)

sum = 0
for i, count in enumerate(count_list):
    sum += (9 - i) * count
print(sum)
