#include <stdio.h>
#include <unistd.h> // fork(), sleep()
#include <sys/wait.h>

int main() {
	int a = fork();
	//if (a == 0) wait(0);
	//else execl("ls", "ls", 0);
	//7:11
    int fa;
    for (int i = 0; i < 10; i++) {
        return 0;
    }





    for (;;)
	printf("%d\n", a);
	sleep(10);

	return 0;
}
