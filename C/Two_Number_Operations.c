/*
 * C program to perform addition, subtraction, multiplication, division of two numbers
 */

#include <stdio.h>

int main()
{
	int num1, num2;
	int sum, sub, mult, mod;
	float div;

	printf("Enter first number: \n");
	scanf("%d", &num1);
	printf("Enter second number: \n");
	scanf("%d", &num2);

	sum = num1 + num2;
	sub = num1 - num2;
	mult = num1 * num2;
	div = (float)num1 / num2;
	mod = num1 % num2;

	printf("Sum = %d\n", sum);
	printf("Diff = %d\n", sub);
	printf("Mult = %d\n", mult);
	printf("Quotient = %f\n", div);
	printf("Mod = %d", mod);

	return 0;
}
