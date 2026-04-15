from sys import stdin
import heapq

input = stdin.readline


def insert(key, min_h, max_h):
    heapq.heappush(min_h, key)
    heapq.heappush(max_h, -key)


def del_min(min_h, min_rm_h, max_rm_h):
    # 제거해야할 최소값(들) 존재
    while len(max_rm_h) != 0 and max_rm_h[0] == min_h[0]:
        heapq.heappop(max_rm_h)
        heapq.heappop(min_h)
    if len(min_h) != 0:
        del_value = heapq.heappop(min_h)
        heapq.heappush(min_rm_h, -del_value)
        return del_value
    return None


def del_max(max_h, min_rm_h, max_rm_h):
    # 제거해야할 최대값(들) 존재
    while len(min_rm_h) != 0 and min_rm_h[0] == max_h[0]:
        heapq.heappop(min_rm_h)
        heapq.heappop(max_h)
    if len(max_h) != 0:
        del_value = -heapq.heappop(max_h)
        heapq.heappush(max_rm_h, del_value)
        return del_value
    return None


for _ in range(int(input())):
    min_h = []
    max_h = []
    min_rm_h = []
    max_rm_h = []
    for _ in range(int(input())):
        cmd, key = input().split()
        if cmd == "I":
            insert(int(key), min_h, max_h)
        elif key == "-1":
            del_min(min_h, min_rm_h, max_rm_h)
        else:
            del_max(max_h, min_rm_h, max_rm_h)
    min_value = del_min(min_h, min_rm_h, max_rm_h)
    max_value = del_max(max_h, min_rm_h, max_rm_h)
    if min_value == None:
        print("EMPTY")
    elif max_value == None:
        print(min_value, min_value)
    else:
        print(max_value, min_value)
