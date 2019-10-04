from ctypes import *

# load lib
mydll = cdll.LoadLibrary("libhello_cpp.dylib")

# call simple fn
print("hello=" + str(mydll.foo()))

# call fn with custom ret type
class POINT(Structure):
    _fields_ = [("x",c_int),("y",c_int)]
bar         = mydll.bar
bar.restype = POINT
abc         = mydll.bar()
print("bar.x=" + str(abc.x) + ",bar.y=" + str(abc.y))

# specifying argtypes
add          = mydll.add
add.argtypes = [c_int, c_int]
add.restype  = c_int
print("3 + 4 = " + str(add(3,4)))
