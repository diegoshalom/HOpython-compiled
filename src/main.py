# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 16:53:23 2016

@author: Nadia
"""

import ctypes as C
math = C.CDLL('./myfirstdl.so')

#defino tipos de inputs y outputs 
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int, C.c_int]

#test add_int y add_float
a=3
b=4
print a,b,math.add_float(a, b)
print a,b,math.add_int(a, b)

#test funciones por referencia
a= C.c_int(3)
b = C.c_int(4)
res = C.c_int()
math.add_int_ref(C.byref(a), C.byref(b), C.byref(res))
print a,b,res.value

a= C.c_float(3)
b = C.c_float(4)
res = C.c_float()
math.add_float_ref(C.byref(a), C.byref(b), C.byref(res))
print a,b,res.value

#test funciones con vectores
in1 = (C.c_int * 3) (1, 2, -5)
in2 = (C.c_int * 3) (-1, 3, 3)
out = (C.c_int * 3) 
math.add_int_array(C.byref(in1), C.byref(in2), C.byref(out),3)
print out[0],out[1],out[3]

in1 = (C.c_float * 3) (1, 2, -5)
in2 = (C.c_float * 3) (-1, 3, 3)
math.dot_product.restype = C.c_float
out=math.dot_product(C.byref(in1), C.byref(in2), 3)

