project(hello_cpp C CXX)
set(SRC lib.cpp)
add_library(hello_cpp SHARED ${SRC})
