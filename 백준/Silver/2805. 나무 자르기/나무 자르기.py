from sys import stdin
input = stdin.readline

def wood_amount(size:int)->int:
    global tree
    sum = 0
    for i in tree:
        if i > size:
            sum += i - size
    return sum

def wood_binary_search(start,end):
    global tree, m
    while end - start > 1:
        mid = (start + end) // 2
        mid_amount = wood_amount(mid)
        if mid_amount >= m:
            start = mid
        else:
            end = mid
    if end - start == 0:
        return end
    else:
        if wood_amount(end) == m:
            return end
        else:
            return start

n,m = map(int,input().split())
tree = list(map(int,input().split()))
max_amount = wood_binary_search(0,max(tree))
print(max_amount)
