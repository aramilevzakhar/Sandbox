#include <stdio.h>

int main() {
	printf("int - %10ld\n", sizeof(int));
	printf("float - %10ld\n", sizeof(float));
	printf("double - %10ld\n", sizeof(double));
	printf("short int- %10ld\n", sizeof(short int));
	printf("signed short - %10ld\n", sizeof(signed short));
	printf("signed short int - %10ld\n", sizeof(signed short int));
	printf("unsigned int - %10ld\n", sizeof(unsigned int));
	printf("long double - %10ld\n", sizeof(long double));
	printf("double - %10ld\n", sizeof(double));
	printf("------------------\n");

	int t = 47;
	int *ptr = &t;

	printf("%p\n", ptr);
	printf("%d\n", *ptr);
	scanf("%d", &t);
	int arr[t];
	
	return 0;
}
