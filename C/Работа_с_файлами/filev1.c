#include <stdio.h>

int main(){
	FILE* fp;
	int n1, n2;
	if ((fp = fopen("input.txt", "r")) == NULL){
		return 0;
	} else{
		fscanf(fp, "%d %d", &n1, &n2);
	}
	fclose(fp);
	printf("%d", n1+n2);

	FILE* fc = NULL;
	if((fc = fopen("output.txt","w"))==NULL){
		return 0;
	}else{
		fprintf(fc, "%d\n", n1+n2);
	}
	fclose(fc);
}
