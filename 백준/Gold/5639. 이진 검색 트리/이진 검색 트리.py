from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
node_list = list(map(int, stdin.read().split()))


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def make_tree(key, start, end):
    cur = Node(key)
    mid = end
    for i in range(start, end):
        if node_list[i] > key:
            mid = i
            break
    if start < mid:
        cur.left = make_tree(node_list[start], start + 1, mid)
    if mid < end:
        cur.right = make_tree(node_list[mid], mid + 1, end)
    return cur


root = make_tree(node_list[0], 1, len(node_list))


def postorder(node):
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.key)


postorder(root)
