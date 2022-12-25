#include <stdio.h>

int main() {
  char word[100];
  int n = 0;
  scanf("%s",&word);
  for (;;){
    for (int i = 0; i < 10; i++){
      printf("%c", word[n]);
      n++;
      if (word[n] == '\0')
        return 0;
      }
    printf("\n");
    }
}