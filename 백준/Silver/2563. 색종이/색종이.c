#include <stdio.h>

int main(){
  char board[100][100] = {0};
  int a;
  scanf("%d",&a);
  for (int i = 0; i < a; i++){
    int x,y;
    scanf("%d%d",&x,&y);
    for (int a = 0; a < 10; a++)
      for (int b = 0; b < 10; b++){
        board[x+a][y+b] = 1;
      }
  }
  int sum = 0;
  for (int i = 0; i < 100; i++)
    for (int j = 0; j < 100; j++){
      if (board[i][j] == 1){
        sum++;
      }
    }
  printf("%d",sum);
}