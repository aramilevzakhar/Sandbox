#include <stdio.h>
#include <malloc.h>

void main(){
	int *arr;
	int cols; // колличество столбецов
	int rows; // колличество рядов
	printf("Entor volue of rows:");
	scanf("%d", &rows);
	printf("Enter volue of cols:");
	scanf("%d", &cols);

	arr = (int*)malloc(rows * cols * sizeof(int));
	for(int i=0;i<rows;i++){
		for(int j=0;j<cols;j++){
			printf("arr[%d][%d] = ", i, j);
			scanf("%d", (arr + i*cols + j));
		}
	}

	for(int i=0;i<rows;i++){
		for(int j=0;j<cols;j++){
			printf("arr[%d][%d] = %d\t", i, j, *(arr + i*cols + j));
		}
		printf("\n");
	}
	free(arr);

}
