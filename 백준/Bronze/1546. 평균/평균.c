#include <stdio.h>

int main(){
  int c;
  scanf("%d",&c);
  int score[c];
  for (int i = 0; i < c; i++){
    scanf("%d", &score[i]);
  }
  int max = 0;
  for (int i = 0; i < c; i++){
    if(score[i] > max) max = score[i];
  }
  double mscore[c];
  for (int i = 0; i < c; i++){
    mscore[i] = (score[i] / (double)max) * 100;
  }
  double msum = 0;
  for (int i = 0; i < c; i++){
    msum += mscore[i];
  }
  printf("%lf",msum / c);
}