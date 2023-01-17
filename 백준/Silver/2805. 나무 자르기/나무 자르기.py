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
    if end - start == 0:
        return end
    elif end - start == 1:
        if wood_amount(end) == m:
            return end
        else:
            return start
    else:
        mid = (start + end) // 2
        mid_amount = wood_amount(mid)
        if mid_amount > m:
            return wood_binary_search(mid,end)
        elif mid_amount == m:
            return wood_binary_search(mid,end)
        else:
            return wood_binary_search(start,mid)

n,m = map(int,input().split())
tree = list(map(int,input().split()))
max_amount = wood_binary_search(0,max(tree))
print(max_amount)
