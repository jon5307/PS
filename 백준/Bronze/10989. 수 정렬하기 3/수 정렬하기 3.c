#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int n, i, j;
    scanf("%d", &n);
    int nums[10000] = {0};
    for (i=0;i<n;i++){
        scanf("%d",&j);
        nums[j-1] += 1;
    }
    for (i=0;i<10000;i++){
        if (nums[i] != 0){
            for (j=0;j<nums[i];j++){
                printf("%d\n",i+1);
            }
        }
    }
    return 0;
}
