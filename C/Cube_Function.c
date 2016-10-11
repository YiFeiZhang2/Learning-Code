#include <stdio.h>

double cube(double num) {
	return (num*num*num);
}

int main(){
	double num, output;

	printf("Enter a number to cube: ");
	scanf("%lf", &num);
	
	output = cube(num);

	printf("Cube is %f\n", output);

	return 0;
}
