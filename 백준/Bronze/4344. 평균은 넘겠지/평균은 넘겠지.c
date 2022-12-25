#include <stdio.h>

int main(){
  int a;
  scanf("%d",&a);
  for (int i = 0; i < a; i++){
    int student;
    int sum = 0;
    scanf("%d",&student);
    int score[student];
    for(int j = 0; j < student; j++){
      scanf("%d",&score[j]);
      sum += score[j];
    }
    double gstudent = 0;
    double average = sum / (double)student;
    for(int j = 0; j < student; j++){
      if (score[j] > average){
        gstudent += 1;
      }
    }
    printf("%.3lf%%\n",(gstudent/student)*100);
  }
}