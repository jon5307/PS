n = int(input())
print("Gnomes:")
for _ in range(n):
    a = list(map(int, input().split()))
    print("Ordered" if a == sorted(a) or a == sorted(a, reverse=True) else "Unordered")
