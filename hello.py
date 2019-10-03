from ctypes import *

class POINT(Structure):
    _fields_ = [("x",c_int),("y",c_int)]

mydll = cdll.LoadLibrary("libhello_cpp.dylib")
print("hello=" + str(mydll.foo()))

mydll.bar.restype = POINT
abc = mydll.bar()
print("bar.x=" + str(abc.x) + ",bar.y=" + str(abc.y))
