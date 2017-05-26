#include <stdio.h>

int main()
{
    char paren;
    int floor = 0;
    while ((paren = fgetc(stdin)) != EOF)
    {
        if (paren == '(') ++floor;
        else if (paren == ')') --floor;
    }
    printf("Floor %d\n", floor);

    return 0;
}
