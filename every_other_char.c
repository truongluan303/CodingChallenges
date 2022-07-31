/*
Implement a C function that takes a null-terminated string and returns
a new heap-allocated null-terminated string containing every other
character from original string (e.g., “house” -> “hue”).
*/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


char* strdup_every_other_char(const char* s)
{
    int len = strlen(s);
    char* result = (char*)malloc((len + 1) * sizeof(char));

    int i = 0;
    int j = 0;
    while (i < len)
    {
        result[j] = s[i];
        i += 2;
        j += 1;
    }
    result[j] = '\0';

    return result;
}



int main()
{
    char string1[] = "123456789";
    char string2[] = "01234567";

    printf(strdup_every_other_char(string1));
    printf("\n");
    printf(strdup_every_other_char(string2));

    return 0;
}
