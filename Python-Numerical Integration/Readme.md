# CSCI-3656

## Coding Assignment (HW6)

This homework asks you to implement two numerical integration methods, described below.
After implementing these methods, you should compare their performance on some test functions with different numbers of points.  Find at least one test function and number of points `n` for which the first method is superior and at least one for which the second is superior.  Display your output using the format
`{testname} {method} {n} {error}`, one per line.
For example, my output might contain
```
sin legendre 3 2.359998e-07
sin legendre 4 -2.679675e-10
```

#### Recursive extrapolation
We have seen how Richardson extrapolation can be used to increase the order of accuracy of Newton-Cotes methods (typically starting with the trapezoid rule).
Implement a method that applies Richardson extrapolation recursively.
You can choose how many times to recurse.

#### Gauss-Legendre integration
The [Integration notebook](http://nbviewer.jupyter.org/github/jedbrown/numerical-computation/blob/master/Integration.ipynb) contains a recursive formula for the derivative of Legendre polynomials.  Write a function `legendre_eval(x, n)` that computes the `n`th Legendre polynomial and its derivative at the points `x`.  Write a function `legendre_roots(n)` that uses Newton's method to compute the roots of the `n`th Legendre polynomial, using the initial guess `cos(linspace(.5/(n-1), 1-.5/(n-1), n) * pi)`.  Write a version of `fint_legendre` (analogous to the implementation in the notebook) that uses the roots that you have computed.
