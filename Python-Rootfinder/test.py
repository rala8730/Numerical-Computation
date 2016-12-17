import numpy
def square(x):
	return x*x

def cube(x):
	return x* square(x)

def xcube_minus2x_sqare_minus2(x):
	#print("f1 function")
	return cube(x) - 2*x - 5

def dv_xcube_minus2x_sqare_minus2(x):
	return 3 *square(x) -2

def seconddv_xcube_minus2x_sqare_minus2(x):
	return 2*3*x
'''
def f2(x):
	return cube(x) *cube(x) -2 

def dv_f2(x):
	return (6 * cube(x) * square(x))  
'''
def arctann(x):
	return numpy.arctan(2*x)

def dv_arctann(x):
	return 2/((4*x**2)+1)

def secdv_arctann(x):
	return 16*x / (4* x**2 + 1)**2

def sinofx_plus_1point1x(x):
	return numpy.sin(x) + 1.1 *x

def dv_sinofx_plus_1point1x(x):
	return numpy.cos(x)+1.1

def secdv_sinofx_plus_1point1x(x):
	return -numpy.sin(x)

testing=[(xcube_minus2x_sqare_minus2,dv_xcube_minus2x_sqare_minus2,seconddv_xcube_minus2x_sqare_minus2),(arctann,dv_arctann,secdv_arctann),(sinofx_plus_1point1x,dv_sinofx_plus_1point1x,secdv_sinofx_plus_1point1x)]