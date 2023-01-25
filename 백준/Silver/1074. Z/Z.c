#include <stdio.h>

int main(void) {
	int n, r, c;
    scanf("%d%d%d",&n,&r,&c);
    int ans = 0;
    for(int i=n-1; i>=0; i--){
        if (r & (1 << i)){
            ans += 1;
            }
        ans <<= 1;
        if (c & (1 << i)){
            ans += 1;
            }
        ans <<= 1;
    }
    printf("%d\n",ans/2);
    return 0;
}
