from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(1000000)


def print_preorder(ios, ioe, pos, poe):
    global inorder, postorder, inorder_position
    if ioe - ios == 0:
        return
    elif ioe - ios == 1:
        print(inorder[ios], end=" ")
    else:
        print(postorder[poe - 1], end=" ")
        mid = inorder_position[postorder[poe - 1]]
        print_preorder(ios, mid, pos, pos + (mid - ios))
        print_preorder(mid + 1, ioe, pos + (mid - ios), poe - 1)


n = int(input())
inorder = list(map(int, input().rstrip().split()))
postorder = list(map(int, input().rstrip().split()))
inorder_position = [0] * (n + 1)
for i in range(n):
    inorder_position[inorder[i]] = i
print_preorder(0, n, 0, n)
