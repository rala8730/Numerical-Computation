# CSCI-3656

## Coding assignment (HW3)

The Householder algorithm uses a reflection to map x to a scaled coordinate vector of the same length, ||x||e_0.  The matrix

```
    [[cos(t), sin(t)], [-sin(t), cos(t)]]
```

is called a **Givens rotation**, rotating the plane by an angle `t`.
Instead of reflecting the vector x to ||x||e_0, it is also possible to rotate it into that position.
Implement a QR algorithm using Givens rotations instead of Householder reflectors.
Recommended steps:

1. Write a function `givens_rot(theta, v, x)` that rotates the vector `x` by an angle `theta` in the subspace spanned by the orthogonal basis `[1, 0, 0, ...]` and `[0, v]` where `v` is a unit vector.
2. Make this function accept a matrix `x` as input, operating on each column independently.
3. Calculate the angle that a vector `x` must be rotated by in order to align with the zeroth axis using the `arctan2` function, e.g., `arctan2(norm(x[1:]), x[0])`.
4. Adapt/port the Householder QR example code to use rotation instead of reflection.  Store the angles `theta` and vectors `v = x[1:]/norm(x[1:])` while triangularizing each column.
5. Write a function `givens_Q_times(V, x)` that applies the action of the orthogonal matrix `Q` (represented as a list `V` of `(theta, v)` pairs) on an input vector (or matrix) `x`.
6. Use `givens_Q_times` with the identity to return the factors `Q` and `R`.

Finally, compute the error in `QR = A` and `Q.T Q = I` where `A` is the Vandermonde matrix associated with m=10 and m=20 equally spaced points on the interval `[-1,1]`.
The output from these two numerical tests should be printed when running `hw3/givens` (or `hw3/givens.py`, `hw3/givens.m`, etc.).
