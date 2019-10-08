#pragma once

extern "C" int foo();

extern "C" struct POINT
{
    int x;
    int y;
    POINT(int x_, int y_) : x(x_), y(y_){}
};
extern "C" POINT bar();

extern "C" int add(int a, int b);

extern "C" int ptr_test(char* v, int len);

extern "C" char* get_bytes(int&);

class Foo
{
public:
    Foo(int x, int y);
    int bar();

private:
    int x;
    int y;
};

extern "C" Foo* Foo_new(int x, int y);
extern "C" int  Foo_bar(Foo*);        
