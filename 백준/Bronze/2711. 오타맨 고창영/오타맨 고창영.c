#include <stdio.h>

int main(){
  int a;
  scanf("%d",&a);
  for(int i = 0; i < a; i++){
    int f;
    char str[81];
    scanf("%d %s",&f, str);
    for (int j = 0; j < 81; j++){
      if (j == f - 1){
        continue;
      }
      else if (str[j] == '\0'){
        break;
      }
      printf("%c",str[j]);
    } 
    printf("\n");
  }
}