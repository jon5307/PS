#include <stdio.h>


int main(void)
{
	int n[8];
	for (int i = 0; i < 8; i++)
	{
		scanf("%d", &n[i]);
	}
	for(int i = 0; i < 8; i++)
	{
		if(n[i] != i+1)
			break;
		if(i == 7){
			printf("ascending");
			return 0;
		}
	}
	for(int i = 0; i < 8; i++)
	{
		if(n[i] != 8-i)
			break;
		if(i == 7){
			printf("descending");
			return 0;
		}
	}
	printf("mixed");
}
