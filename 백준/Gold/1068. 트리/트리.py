from sys import stdin
input = stdin.readline

n = int(input())
child = [[] for _ in range(n)]
root = None

parent_list = list(map(int,input().rstrip().split()))
remove = int(input())

for idx, parent in enumerate(parent_list):
    if parent == -1:
        root = idx
    else:
        child[parent].append(idx)



def dfs(node):
    if len(child[node]) == 0:
        return 1
    else:
        sum = 0
        for i in child[node]:
            sum += dfs(i)
        return sum

if parent_list[remove] != -1:
    child[parent_list[remove]].remove(remove)
    print(dfs(root))
else:
    print(0)
    