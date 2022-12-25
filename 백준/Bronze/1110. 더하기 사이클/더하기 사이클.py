num = int(input())
count = 0
if num != 0:
    out = (num // 10 + num % 10) % 10 + 10 * (num % 10)
    count += 1
    while num != out:
        out = (out // 10 + out % 10) % 10 + 10 * (out % 10)
        count += 1
    print(count)
else:
    print(1)