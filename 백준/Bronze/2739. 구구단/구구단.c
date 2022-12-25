#include <stdio.h>

int main() {
  int i;
  scanf("%d",&i);
  for (int j = 1; j <=9; j++) {
    printf("%d * %d = %d\n",i,j,i*j);
  }
}