#include <stdio.h>
#include <math.h>

int main(){
    int sh, sm, ss, eh, em, es;
    scanf("%d : %d : %d", &sh, &sm, &ss);
    scanf("%d : %d : %d", &eh, &em, &es);
    int ds = es - ss;
    if (ds < 0){
        em--;
        ds += 60;
    }
    int dm = em - sm;
    if (dm < 0){
        eh--;
        dm += 60;
    }
    int dh = eh - sh;
    if (dh < 0){
        dh += 24;
    }
    printf("%d", dh*3600+dm*60+ds);
    return 0;
}