#include <stdio.h>

int main(void) {
  int a;
  scanf("%d",&a);
  for(int i=a;i>=1;i--) {
    for(int j=1;j<=a-i;j++){
      printf(" ");
    }
    for(int j=1;j<=i*2-1;j++){
      printf("*");
    }
    printf("\n");
  }
}