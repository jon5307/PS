#include <stdio.h>

int main(){
    int N;
    scanf("%d",&N);
    int bag = N/5;
    int left = N%5;

    while(1){
        if (left > N){
            bag = -1;
            break;
        }
        else if (left % 3 == 0){
            bag += left / 3;
            break;
        }
        else{
            left += 5;
            bag--;
        }
    }

    printf("%d\n",bag);
}