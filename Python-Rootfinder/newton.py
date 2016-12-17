#!/usr/bin/env python3 
import math 
import numpy
import test

#from test import *
#newtons method 
numpy.seterr(all='ignore')

def newtons_method(x,n,f,dev_f):

	for i  in range (1,n):
		b= f(x)
		c=dev_f(x)
		x0=x-(b/c)
		x=x0
		print(f.__name__,i,x,b)
	return x

for f in test.testing:
	print(" ")
	newtons_method(3,15,f[0],f[1])
