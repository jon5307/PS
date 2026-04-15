from sys import stdin

input = stdin.readline

n, s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
# a~b까지 합은 prefix[b+1]-prefix[a]
prefix = [0]
for i in range(n):
    prefix.append(prefix[-1] + arr[i])

start = 0
end = 1
min_len = 1000000
while True:
    subtotal = prefix[end] - prefix[start]
    if end == n and subtotal < s:
        break
    if subtotal >= s:
        min_len = min(min_len, end - start)
        start += 1
    else:
        end += 1
print(min_len if min_len < 1000000 else 0)
