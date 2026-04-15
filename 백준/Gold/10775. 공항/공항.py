from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)


def find_root(node):
    if node != parent[node]:
        parent[node] = find_root(parent[node])  # 경로 압축
    return parent[node]


G = int(input())
P = int(input())
gi = [int(input()) for _ in range(P)]
parent = [i for i in range(G + 1)]


def docking(plane, docked):
    if plane == P:
        return docked
    global gi
    dock_location = find_root(gi[plane])
    if dock_location == 0:
        return docked
    else:
        parent[dock_location] = dock_location - 1
        return docking(plane + 1, docked + 1)


print(docking(0, 0))
