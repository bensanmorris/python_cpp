# -----
# Notes
# -----
# str(x)  - is the human readable representation of x (calls object's __str__) impl
# repr(x) - is the developer representation of x (calls object's __repr__) impl
# ----

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
print("ptr_test = " + str(buffer.value))

# allocating and returning byte data from cpp -> python
INT_POINTER        = POINTER(c_int)
CHAR_POINTER       = POINTER(c_char)
get_bytes          = mydll.get_bytes
get_bytes.argtypes = [INT_POINTER]
get_bytes.restype  = CHAR_POINTER
size               = c_int(0)
retval             = get_bytes(byref(size))
print(size)
print(retval)
for i in range(size.value):
    print(retval[i])

# using a standard cpp class
class Foo(object):
    def __init__(self,x,y):
        self.obj = mydll.Foo_new(x,y)
    def bar(self):
        return mydll.Foo_bar(self.obj)

foo = Foo(1,2)
print(str(foo.bar()))
