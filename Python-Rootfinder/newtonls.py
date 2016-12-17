#!/usr/bin/env python3 
#newtons ls 
import numpy
import test

def newtonsls(x,n,f,dev_f):
	for i in range (0,n):
		b=f(x)
		c=dev_f(x)

		scale=0.5
		var2=abs(b)
		x0=x-(b/c)
		var1=abs(f(x0))
		if ((abs(b)<(1e-12))):
			return 1
		while(var2 <= var1):
			x0= x - (scale*(b/c))
			var1=abs(f(x0))
			scale/=2
		x=x0
		print(f.__name__,i,x,b)
	return x
for f in test.testing:
	print(" ")
	newtonsls(3,15,f[0],f[1])


