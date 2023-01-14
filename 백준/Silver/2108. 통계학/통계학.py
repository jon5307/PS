from sys import stdin
input = stdin.readline

N = int(input())
nums = []
freq = {}
sum = 0
for _ in range(N):
    a = int(input())
    sum += a
    nums.append(a)
    if a in freq:
        freq[a] += 1
    else:
        freq[a] = 1

nums.sort()

a = sorted([k for k,v in freq.items() if max(freq.values()) == v])
if len(a) == 1:
    mode = a[0]
else:
    mode = a[1]
print(round(sum/N))
print(nums[N//2])
print(mode)
print(nums[-1]-nums[0])
