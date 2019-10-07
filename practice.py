from ctypes import *

# custom type
class Foo(Structure):
    _fields_ = [("x",c_int),("y",c_int)];
    def __str__(self):
        return str.format("x = {}, y = {} ",self.x, self.y)
    
# allocate and print
foo = Foo(1,2)
print(str.format("str(foo) is: {}, repr(foo) is: {}", str(foo), repr(foo)))
