#include <stdio.h>

int main() {
  char word[50];
  int a;
  scanf("%d",&a);
  for (int i = 0; i < a; i++){
    scanf("%s",&word);
    printf("String #%d\n",i+1);
    for (int n = 0; n < 50; n++){
      if(word[n] == '\0')
        break;
      printf("%c",word[n]==90?65:word[n]+1);
    }
    printf("\n\n");
  }
}