#include <unistd.h> // For setuid()
#include <stdlib.h> // For system()

int main()
{
	setuid(0);
	system("/bin/sh");
	return 0;
}
