#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>


int main() {
	int s;
	s = socket(AF_INET, SOCK_STREAM, 0);
	//struct hostent* server;
	const struct sockaddr* server;
	server = gethostbyname("192.168.1.108");

	bind(s, server, 13);

	return 0;
}











