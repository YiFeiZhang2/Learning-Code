#include<stdio.h>

int main(void){
	int num1, num2;
	int larger;
	printf("Enter the first number:\n");
	scanf("%d", &num1);
	printf("Enter the second number:\n");
	scanf("%d", &num2);

	if (num1 > num2) {
		larger = num1;
	} else {
		larger = num2;
	}

	printf("%d", larger);
	return larger;
}
