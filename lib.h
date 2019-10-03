#pragma once

extern "C" int foo();

extern "C" struct POINT
{
    int x;
    int y;
    POINT(int x_, int y_) : x(x_), y(y_){}
};
extern "C" POINT bar();
