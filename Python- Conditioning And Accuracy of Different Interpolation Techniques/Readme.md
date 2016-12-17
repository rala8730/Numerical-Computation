# CSCI-3656

## Coding Assignment (HW4)

This homework explores the concepts of conditioning and accuracy of different interpolation techniques.  The [Interpolation notebook](https://nbviewer.jupyter.org/github/jedbrown/numerical-computation/blob/master/Interpolation.ipynb) has some code that may be useful to get you started.  The step below asks you to print some lines with the given format strings.  These are C (or Python, etc.) style format strings, `%d` means decimal integer and `%e` means floating point in scientific notation.  Please make your code print these lines as described when I execute `hw4/run` (or `hw4/run.py`, `hw4/run.m`, etc.).

1. Write a function `piecewise_linear_interp_and_eval(x, xx)` that returns a matrix mapping the values of a function at the points `x` to the values of the interpolating function at `xx`.  This function is analogous to `chebyshev_interp_and_eval(x, xx)`.  Print the norm (largest singular value) of this matrix for each of `x = linspace(-1,1,20)` and `x = cosspace(-1,1,20)` with `xx = linspace(-1,1,100)`.  Use the format strings `"piecewise_linear linspace -> linspace: norm=%e"` and `"piecewise_linear cosspace -> linspace: norm=%e"` for these two lines.
2. Implement/copy/port `chebyshev_interp_and_eval` to your source file (same as above, but using a single Chebyshev polynomial instead of piecewise linear functions).  Print the norms as above (replacing `piecewise_linear` with `chebyshev`).
3. For the function `f(x) = exp(-16*x**2)`, determine the number `n` of `x=linspace(-1,1,n)` and `x=cosspace(-1,1,n)` points needed to make the maximum interpolation error at `xx` less than `eps=1e-4`.  I expect you will write a loop that terminates when this condition is met or if no solution is found at `n=100`.
(This maximum error is also known as the "infinity norm". It is an option for the `norm` function in most linear algebra libraries.)  Print the number of points and the error using the format string `"piecewise_linear f() cosspace -> linspace: n=%d max_error=%e"` (and similar for `linspace`).
4. Same as above for `g(x) = abs(x)` and `eps=1e-2` (replace `f()` with `g()` in the format string).
