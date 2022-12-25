#include <stdio.h>

int main() {
  int num[10], rem[42] = {0}, amount = 0;
  for (int i = 0; i < 10; i++){
    scanf("%d",&num[i]);
  }
  for (int i = 0; i < 10; i++){
    rem[num[i] % 42] += 1;
  }
  for (int i = 0; i < 42; i++){
    if(rem[i] != 0){
      amount++;
    }
  }
  printf("%d",amount);
  
}