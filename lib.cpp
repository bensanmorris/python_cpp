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

char* get_bytes(int& len)
{
    int   n      = 4;
    char* retval = new char[n];
    for(int i = 0; i < n; ++i)
        retval[i] = 'a' + i;
    len = n;
    return retval;
}

Foo::Foo(int x_, int y_) : x(x_), y(y_)
{
}

int Foo::bar()
{
    return x + y;
}

Foo* Foo_new(int x, int y)
{
    return new Foo(x,y);
}

int Foo_bar(Foo* foo)
{
    return foo->bar();
}

