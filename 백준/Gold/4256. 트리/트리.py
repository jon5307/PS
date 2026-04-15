from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(1000000)


def print_postorder(pos, poe, ios, ioe):
    global preorder, inorder, inorder_position
    if ioe - ios == 0:
        return
    elif ioe - ios == 1:
        print(inorder[ios], end=" ")
    else:
        mid = inorder_position[preorder[pos]]
        print_postorder(pos + 1, pos + mid - ios + 1, ios, mid)
        print_postorder(pos + mid - ios + 1, poe, mid + 1, ioe)
        print(preorder[pos], end=" ")


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().rstrip().split()))
    inorder = list(map(int, input().rstrip().split()))
    inorder_position = [0] * (n + 1)
    for i in range(n):
        inorder_position[inorder[i]] = i
    print_postorder(0, n, 0, n)
    print()
