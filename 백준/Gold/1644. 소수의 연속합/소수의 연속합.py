n = int(input())

if n == 1:
    print(0)
    exit(0)
is_prime = [True for _ in range(n + 1)]
for i in range(2, int(n ** (1 / 2)) + 1):
    if is_prime[i]:
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1

prime = []
for i in range(2, n + 1):
    if is_prime[i]:
        prime.append(i)

start = 0
end = 0
sum_nums = prime[0]
count = 0
while start < len(prime) and end < len(prime):
    if sum_nums < n:
        end += 1
        if end < len(prime):
            sum_nums += prime[end]
    elif sum_nums == n:
        count += 1
        end += 1
        if end < len(prime):
            sum_nums += prime[end]
    else:
        sum_nums -= prime[start]
        start += 1
        if start > end:
            end = start
            if end < len(prime):
                sum_nums = prime[end]
print(count)
