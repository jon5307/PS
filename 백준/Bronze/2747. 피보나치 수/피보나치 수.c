#include <stdio.h>

int main(){
  int n, a = 0, b = 1;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    if (i % 2 == 0)
      a += b;
    else
      b += a;
  }
  if (n % 2 == 0)
    printf("%d",a);
  else
    printf("%d",b);
}