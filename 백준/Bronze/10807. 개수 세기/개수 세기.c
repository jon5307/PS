#include <stdio.h>

int main() {
  int n;
  scanf("%d",&n);
  int arr[n];
  for (int i = 0; i < n; i++){
    scanf("%d", &arr[i]);
  }
  int v, count = 0;
  scanf("%d",&v);
  for (int i = 0; i < n; i++){
    if (arr[i] == v){
      count++;
    }
  }
  printf("%d",count);
}