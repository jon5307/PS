#include <stdio.h>

int main() {
  int a,b,c;
  scanf("%d%d%d",&a,&b,&c);
  if (a < b && a < c) {
    printf("%d ",a);
    if (b < c) {
      printf("%d %d",b,c);
    }
    else {
      printf("%d %d",c,b);
    }
  }
  else if (b < a && b < c) {
    printf("%d ",b);
    if (a < c) {
      printf("%d %d",a,c);
    }
    else {
      printf("%d %d",c,a);
    }
  }
  else {
    printf("%d ",c);
    if (b < a) {
      printf("%d %d",b,a);
    }
    else {
      printf("%d %d",a,b);
    }
  }
  
  
}