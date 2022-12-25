#include <stdio.h>

int main(){
  int a;
  scanf("%d",&a);
  int i,j;
  for (i = 0; i < a; i++){
    // blank
    for (j = 0; j < a - i - 1; j++)
      printf(" ");
    for (j = 0; j < 2 * i + 1; j++)
      printf("*");
    printf("\n");
  }
  for (i = 0; i < a - 1; i++){
    for (j = 0; j < i + 1; j++)
      printf(" ");
    for (j = 0; j < 2 * (a - i) - 3; j++)
      printf("*");
    printf("\n");
  }
}