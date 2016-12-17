#!/usr/bin/env python3 
#cubic
#from test import *
import numpy
import test
numpy.seterr(all='ignore')

def cubicpos(a,n,f,dev_f,secdev_f):
	for i in range(1,n):
		b= f(a)
		c=dev_f(a)
		d=secdev_f(a)
		x= ((-c + (numpy.sqrt((c**2) - (2*d*b))))/d) +a
		a=x 
		print(f.__name__,i,x,b)

for f in test.testing:
	print(" ")
	cubicpos(3,15,f[0],f[1],f[2])




