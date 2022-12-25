#include <stdio.h>

int main() {
  char word[80];
  int a;
  scanf("%d",&a);
  for (int i = 0; i < a; i++){
    int bonus = 0, score = 0;
    scanf("%s",&word);
    for (int j = 0;;j++){
      if (word[j] == 'O'){
        score += 1 + bonus;
        bonus++;
      }
      else if (word[j] == 'X'){
        bonus = 0;
      }      
      if (word[j+1] == '\0'){
        printf("%d\n",score);
        break;
      }
    }
  }
}