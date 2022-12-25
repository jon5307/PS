#include <stdio.h>

int main() {
  int at[30] = {0};
  int n;
  for (int i = 0; i < 28; i++){
    scanf("%d",&n);
    at[n-1] = 1;
  }
  for (int i = 0; i < 30; i++){
    if(!at[i]){
      printf("%d\n",i+1);
    }
  }
}