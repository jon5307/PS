#include <stdio.h>

int main(void) {
	int n, r, c;
    scanf("%d%d%d",&n,&r,&c);
    int ans = 0;
    for(int i=1<<n; i!=0; i>>=1){
        ans <<= 1;
        if (r & i)
            ans += 1;
        ans <<= 1;
        if (c & i)
            ans += 1;
    }
    printf("%d\n",ans);
    return 0;
}