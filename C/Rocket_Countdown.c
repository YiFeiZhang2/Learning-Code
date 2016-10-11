#include <stdio.h>

int main(void){
	int n;
	printf("How big is the rocket countdown?\n");
	scanf("%d", &n);
	for (int i = n; i>0; i--) {
		printf("%d\n", i);
	}
	printf("Blast Off!\n");
	return 0;
}
