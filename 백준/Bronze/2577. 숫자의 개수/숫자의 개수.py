a = int(input())
b = int(input())
c = int(input())
ans = str(a * b * c)
table = [0 for _ in range(10)]
for i in ans:
    table[int(i)] += 1
for i in range(10):
    print(table[i])
