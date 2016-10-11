/*
 * C program to ask for input of two numbers, and then print the sum of them
 */

#include <stdio.h>

int main()
{
	int num1, num2;
	printf("Input first number\n");
	scanf("%d", &num1);
	printf("Input second number\n");
	scanf("%d", &num2);
	
	int sum = num1 + num2;

	printf("%d\n", sum);
	return sum;
}
