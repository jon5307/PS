#include <stdio.h>
#include <math.h>

int main(){
    int c;
    scanf("%d", &c);
    for (int i=0; i<c; i++){
        int bs;
        scanf("%d", &bs);
        int person = 1;
        for(int i=0; i<bs-1;i++){
            person = 2*(person)+1;
        }
        printf("%d\n", person);
    }
    return 0;
}