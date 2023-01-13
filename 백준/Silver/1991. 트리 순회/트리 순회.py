from sys import stdin,stdout
input = stdin.readline
print = stdout.write
from collections import namedtuple

Node = namedtuple("Node", "item left right")

def preorder(item):
    global tree
    _,left,right = tree[item]
    print(item)
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

def inorder(item):
    global tree
    _,left,right = tree[item]
    if left != '.':
        inorder(left)
    print(item)
    if right != '.':
        inorder(right)

def postorder(item):
    global tree
    _,left,right = tree[item]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(item)

tree = {}
for _ in range(int(input())):
    item,left,right = input().rstrip().split()
    tree[item] = Node(item,left,right)

preorder('A')
print('\n')
inorder('A')
print('\n')
postorder('A')
print('\n')
