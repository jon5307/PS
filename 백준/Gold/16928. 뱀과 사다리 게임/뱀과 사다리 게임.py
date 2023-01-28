from sys import stdin
input = stdin.readline


u,v = map(int,input().split())
board = [i for i in range(101)]
dice_cnt = [-1 for _ in range(101)]
dice_cnt[1] = 0
for _ in range(u+v):
    start, end = map(int,input().split())
    board[start] = end

queue = [1]
while queue:
    curr = queue.pop(0)
    curr_cnt = dice_cnt[curr]
    if curr <= 94:
        for i in range(curr+1,curr+7):
            dest = board[i]
            dest_cnt = dice_cnt[dest]
            if dest_cnt == -1:
                dice_cnt[dest] = curr_cnt + 1
                queue.append(dest)
            elif dest_cnt > curr_cnt + 1:
                dice_cnt[dest] = curr_cnt + 1
                queue.append(dest)
    else:
        for i in range(curr+1,101):
            dest = board[i]
            dest_cnt = dice_cnt[dest]
            if dest_cnt == -1:
                dice_cnt[dest] = curr_cnt + 1
                queue.append(dest)
            elif dest_cnt > curr_cnt + 1:
                dice_cnt[dest] = curr_cnt + 1
                queue.append(dest)


print(dice_cnt[100])
