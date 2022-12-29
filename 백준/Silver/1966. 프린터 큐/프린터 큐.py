from collections import deque
from dataclasses import dataclass
import sys
input = sys.stdin.readline

@dataclass(order=True)
class Docs:
    prio: int
    want: bool = False

def solve():
    amount, M = map(int,input().split())
    p = deque(map(int,input().split()))
    q = deque()
    for i in range(amount):
        if i != M:
            q.append(Docs(prio = p.popleft()))
        else:
            q.append(Docs(prio = p.popleft(), want = True))
    printed_amount = 0
    while True:
        first_docs = q.popleft()
        post = False
        for _ in range(amount - 1):
            check_docs = q.popleft()
            if not post and first_docs.prio < check_docs.prio: # first docs should postponed
                post = True
            q.append(check_docs)
        if post:
            q.append(first_docs)
        elif not first_docs.want:
            amount -= 1
            printed_amount += 1
        else:
            print(printed_amount+1)
            break

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
