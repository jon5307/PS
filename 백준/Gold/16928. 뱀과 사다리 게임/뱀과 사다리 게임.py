from sys import stdin
input = stdin.readline


u,v = map(int,input().split())
board = [i for i in range(101)] # snake and ladder
dice_cnt = [-1 for _ in range(101)] # number of dice rolled
dice_cnt[1] = 0
for _ in range(u+v):
    start, end = map(int,input().split())
    board[start] = end

queue = [1]
while queue:
    curr = queue.pop(0)
    curr_cnt = dice_cnt[curr]
    start = curr + 1
    end = curr+7 if curr <= 94 else 101

    for i in range(start,end):
        dest = board[i]
        dest_cnt = dice_cnt[dest]
        if dest_cnt == -1 or dest_cnt > curr_cnt + 1: # never visited or found shorter route
            dice_cnt[dest] = curr_cnt + 1
            queue.append(dest)

print(dice_cnt[100])