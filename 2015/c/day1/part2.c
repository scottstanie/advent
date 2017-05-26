#include <stdio.h>

int main()
{
    char paren;
    int floor = 0, position = 0;

    while ((paren = fgetc(stdin)) != EOF)
    {
        ++position;
        if (paren == '(')
            ++floor;
        else if (paren == ')')
        {
            --floor;
            if (floor < 0)
            {
                printf("Done: position of floor < 0: %d\n", position);
                break;
            }
        }
    }

    return 0;
}
