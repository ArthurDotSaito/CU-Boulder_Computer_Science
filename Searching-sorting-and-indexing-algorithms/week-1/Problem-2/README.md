## Problem 2 (Find integer cube root.)

The integer cube root of a positive number $n$ is the smallest number $i$ such that $i^3 \leq n$ but $(i+1)^3 > n$.

For instance, the integer cube root of $100$ is $4$ since $4^3 \leq 100$ but $5^3 > 100$. Likewise, the integer cube root of $1000$ is $10$.

Write a function `integerCubeRootHelper(n, left, right)` that searches for the integer cube-root of `n` between `left` and `right` given the following pre-conditions:

- $n \geq 1$
- $\text{left} < \text{right}$.
- $\text{left}^3 < n$
- $\text{right}^3 > n$.
