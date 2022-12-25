#include <stdio.h>

int main() {
  int a, result = 1;
  scanf("%d",&a);
  while (a != 0) {
    result *= a;
    a--;
  }
  printf("%d", result);
}