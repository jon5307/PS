#include <stdio.h>
#include <string.h>

void add_sum(char* a, char* b, char* sum);

int main() {
	char a[100000], b[100000], sum[100000];
	scanf("%s %s",a, b);
	add_sum(a,b,sum);
	printf("%s", sum);
	return 0;
}

void add_sum(char *a, char *b, char *sum) {
  int a_len = strlen(a);
  int b_len = strlen(b);
  int big_len, small_len;
  char *big, *small;
  char r_sum[10001];
  if (a_len > b_len) {
    big = a;
    small = b;
    big_len = a_len;
    small_len = b_len;
  }
  else {
    big = b;
    small = a;
    big_len = b_len;
    small_len = a_len;
  }
  int up = 0;
  for (int i = 0; i < big_len; i++) {
    int alpha = (int)(big[big_len-i-1] - '0');
    int beta = small_len <= i ? 0 : (int)(small[small_len-i-1] - '0');
    r_sum[i] = (char)((alpha+beta+up) % 10) + '0';
    up = (alpha + beta + up) / 10;
  }
  int sum_len;
  if (up == 0){
    sum_len = big_len;
  }
  else {
    sum_len = big_len+1;
    r_sum[big_len] = (char)(up) + '0';
  }
  for (int i = 0; i < sum_len; i++) {
    sum[i] = r_sum[sum_len-i-1];
  }
  return;
}