#include <stdio.h>

int main() {
  char word[101];
  scanf("%s",word);
  int len = 0;
  for(int i = 0; i < 100;i++){
    if(word[i] == '\0')
      break;
    else
      len++;
  }
  printf("%d",len);
}