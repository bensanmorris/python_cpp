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

# specifying a python fn as the restype of a cpp fn
def check_retval(val):
    if(val == 7):
        return "Bingo"
    return "No dice"
add.restype = check_retval
print("3 + 4 = " + str(add(3,4)))

# passing by ref
ptr_test          = mydll.ptr_test
ptr_test.argtypes = [c_char_p,c_int]
ptr_test.restype  = c_int
buffer_len        = 4
buffer            = create_string_buffer(buffer_len)
retval            = ptr_test(buffer, buffer_len)
print(str(retval))
print(buffer)
print(buffer.value)
print(repr(buffer.value))
print("ptr_test = " + repr(buffer.value))
