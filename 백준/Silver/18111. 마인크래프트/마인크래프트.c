#include <stdio.h>
#include <stdlib.h>

int main(){
    int x,y,block;
    scanf("%d%d%d",&x,&y,&block);
    int max = 0, min = __INT_MAX__;
    int **world = (int **)malloc(sizeof(int*)*x);
    for (int i=0; i<x; i++){
        world[i] = (int *)malloc(sizeof(int)*y);
        for (int j=0; j<y; j++){
            scanf("%d", &world[i][j]);
            if(min > world[i][j]) min = world[i][j];
            if(max < world[i][j]) max = world[i][j];
        }
    }
    
    // 계산
    long long int time = __INT_MAX__, height;
    for (int ch=min; ch<=max; ch++){
        // 블록마다 돌면서 시간 계산
        int rem_blo = block;
        long long int cur_time = 0;
        for (int i=0; i<x; i++){
            for (int j=0; j<y; j++){
                int diff_block = world[i][j] - ch;
                rem_blo += diff_block;
                // 블록을 쌓아야함
                if (diff_block < 0){
                    cur_time -= diff_block; 
                }
                // 블록을 깎아야함
                else{
                    cur_time += diff_block * 2;
                }

            }
        }
        if (rem_blo >= 0 && time >= cur_time){
            time = cur_time;
            height = ch;
        }
    }
    printf("%d %d\n", time, height);
    return 0;
}