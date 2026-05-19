#include "string.h"
#include "stdio.h"

void main()
{
    char buf[50];
    sprintf(buf, "Hallo");
    for(int x = 0; x < 10; x++)
    {
        printf("%s\n", buf);
    }

    int y = 0;
    while(y < 10)
    {
        printf("%s\n", buf);
        y++;
    }

    int z = 0;

    do
    {
       printf("%s\n", buf);
        z++; 
    }
    while (z < 10);

    int u = 10;
    int *p = &u;
    (*p)++;
    printf("%i\n", u);
}


