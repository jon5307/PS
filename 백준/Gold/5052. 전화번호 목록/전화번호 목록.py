from sys import stdin

input = stdin.readline


class Node:
    def __init__(self):
        self.child = [None for _ in range(10)]
        self.has_child = False

    def add_child(self, num):
        if self.child[num] == None:
            self.child[num] = Node()
            self.has_child = True
            return True
        return False


def solve():
    root = Node()
    phonebook = [input().strip() for _ in range(int(input()))]
    phonebook.sort(key=lambda i: len(i))
    cur = root
    for i in map(int, phonebook[0]):
        cur.add_child(i)
        cur = cur.child[i]
    for phone_num in phonebook[1:]:
        cur = root
        new_path = False
        for i in map(int, phone_num):
            if not cur.has_child and not new_path:
                print("NO")
                return
            if cur.child[i] == None:
                cur.add_child(i)
                new_path = True
            cur = cur.child[i]
    print("YES")
    return


for _ in range(int(input())):
    solve()
