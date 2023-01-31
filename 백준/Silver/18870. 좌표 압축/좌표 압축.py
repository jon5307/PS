from sys import stdin
input = stdin.readline


n = int(input())
orig_coord = list(map(int,input().split()))
sorted_coord = list(set(orig_coord))
sorted_coord.sort()

dic = {sorted_coord[i]:i for i in range(len(sorted_coord))}

print(*[dic[i] for i in orig_coord])
