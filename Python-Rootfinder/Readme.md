# CSCI-3656


## Coding assignment 1

1. Write a program `hw1/newton` that implements Newton's method and runs it on some test equations of your choice.  Output the convergence history for each test equation (please use the format described below).
2. Find a *strictly* monotonically increasing function with a unique root for which Newton's method diverges for initial guess x=1.0.  Add this to your test set.
3. Newton's method is often paired with a "line search" that scales the step size by a factor such that the norm of the new residual is smaller than the previous.  I.e., find a scaling factor such that `|f(x_{n+1})| < |f(x_n)|` where `x_{n+1} = x_n - scale * f(x)/f'(x)`.  One of the simplest variants is to start with a scaling factor of 1 and cut it in half until the norm decreases.  Implement this variant in `hw1/newtonls` and run it on your test equations.
4. Newton's method is based on dropping the quadratic and higher terms in a Taylor expansion.  Write a program `hw1/cubic` that implements a method that keeps the quadratic term in the Taylor expansion (dropping cubic and higher terms).  You will need to make choices about multiple roots or non-existant roots; we discussed some options in class.  Find an equation for which Newton is better and an equation for which the cubic algorithm is better.  (Better means that an algorithm converges faster or converges when the other diverges.)  Add these to your test suite.
<!--
### Edits (posted 2016-09-08)

* Update part 2 to request *strict* monotonicity (i.e., the derivative is never zero).  You can use a function that is defined for all real numbers `x`, but that is not required.
* Explain scaling factor for the line search in more detail and clarify choices in the cubic algorithm.

### Notes
* When executed, each of the three programs (`hw1/newton`, `hw1/newtonls`, and `hw1/cubic`) should print a sequence of lines containing the following information for each equation in your test suite.

```
${EquationName} ${IterationNumber} ${CurrentX} ${Residual}
```

(The `${VariableName}` syntax above indicates variable expansion; the `$`, `{`, and `}` characters are not printed.)
The `EquationName` is any (string) key you choose, it just allows comparison between the different programs.
Let `IterationNumber` start at 0 with the initial guess.
`CurrentX` and `Residual` are floating point values -- format them in a way that you think is appropriate.

* You can put your test equations in a separate file that is included or imported by each of the three executables.

* Be sure to commit and push all necessary source code to make your programs run.

* I will run `make` before trying to run the executables.  If you are using a compiled language, please write a [GNU-style makefile](https://www.gnu.org/software/make/manual/make.html#Introduction) (`hw1/Makefile`) to build your executables.

* You may use libraries such as SymPy to compute derivatives for this assignment.
Please note, however, that f(x) could be an arbitrary function (it could have its own solves inside, table lookups, etc.)
Also, we'll see in class how the output of symbolic differentiation expression grows exponentially in the size of the input.
So symbolic differentiation is not a general purpose solution despite being very useful for testing.
-->
