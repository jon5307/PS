#include <stdio.h>
#include <math.h>

int main() {
  int amount = 0;
  int repeat;
  scanf("%d",&repeat);
  for (int i = 1; i<=repeat; i++) {
    int length = log10(i)+1;
    if (length == 1 || length == 2 || (i%10) + (int)(i/100) == 2 * (int)((i % 100) / 10))
      amount++;
      
  }
  printf("%d\n",amount);
}