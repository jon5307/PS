orig_x, orig_y = map(int,input().split())
orig_board = [[0 for _ in range(orig_y)] for _ in range(orig_x)]

for i in range(orig_x):
    line = input()
    for j in range(orig_y):
        if line[j] == "B":
            orig_board[i][j] = 1

min_rect = 64
            
# first is white
for i in range(orig_x - 7):
    for j in range(orig_y - 7):
        w_rect_count = 0
        b_rect_count = 0
        timing = 0
        
        for k in range(i,i+8):
            for l in range(j,j+8):
                if orig_board[k][l] != timing:
                    w_rect_count += 1
                if orig_board[k][l] == timing:
                    b_rect_count += 1
                timing = (timing + 1) % 2
            timing = (timing + 1) % 2
        
        if min_rect > w_rect_count:
            min_rect = w_rect_count
        if min_rect > b_rect_count:
            min_rect = b_rect_count

print(min_rect)
                    