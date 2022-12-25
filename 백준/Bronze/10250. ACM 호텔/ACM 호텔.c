#include <stdio.h>

int main() {
  int ca, h, w, n, x, y;
  scanf("%d", &ca);
  for (int i = 0; i < ca; i++) {
    scanf("%d%d%d", &h, &w, &n);
    // room
    x = n / h + 1;
    // floor
    y = n % h;
    if (y==0){
      y = h;
      x--;
    }
    printf("%d%02d\n", y, x);
  }
}