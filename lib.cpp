#include "lib.h"
#include <string>

int foo()
{
    return 7;
}

POINT bar()
{
    return POINT(7,11);
}

int add(int a, int b)
{
    return a + b;
}

int ptr_test(char* v, int len)
{
    for(int i = 0; i < len; ++i)
        v[i] = 'a' + i;
    v[len] = '\0';
    return 0;
}
