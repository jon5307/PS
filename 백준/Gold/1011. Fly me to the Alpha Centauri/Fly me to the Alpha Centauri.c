#include <stdio.h>
#include <math.h>

int main(){
    int c;
    scanf("%d", &c);
    for (int i=0; i<c; i++){
        int x,y,distance;
        scanf("%d %d", &x, &y);
        distance = y-x;
        int speed = sqrt(distance);
        int count = 0;

        while((speed+1)*speed >= distance){
            speed--;
        }
        speed++;
        count += (speed-1) * 2;
        distance -= (speed-1) * speed;

        while(distance != 0){
            if (distance >= speed){
                count += distance / speed;
                distance = distance % speed;
            }
            speed--;
        }
        printf("%d\n", count);
    }
    return 0;
}