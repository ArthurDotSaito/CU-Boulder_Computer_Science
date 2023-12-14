## Problem 1: Find Crossover Indices.

You are given data that consists of points
$(x_0, y_0), \ldots, (x_n, y_n)$, wherein $x_0 < x_1 < \ldots < x_n $, and  $y_0 < y_1 \ldots < y_n$ as well.

Furthermore, it is given that $y_0 < x_0$ and $ y_n > x_n$.

Find a "cross-over" index $i$ between $0$ and $n-1$ such that $ y*i \leq x_i$ and $y*{i+1} > x\_{i+1}$.

Note that such an index must always exist (convince yourself of this fact before we proceed).

**Example**

$$
\begin{array}{c| c c c c c c c c c }
i & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
x_i & 0 & 2 & 4 & \color{red}{5} & \color{red}{6} & 7 & 8 & 10 \\
y_i & -2 & 0 & 2 & \color{red}{4} & \color{red}{7} & 8 & 10 & 12 \\
\end{array}
$$

The algorithm must find the index $i=3$ as the crossover point.

On the other hand, consider the data

$$
\begin{array}{c| c c c c c c c c c }
i & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
x_i & \color{red}{0} & \color{red}{1} & 4 & \color{red}{5} & \color{red}{6} & 7 & 8 & 10 \\
y_i & \color{red}{-2} & \color{red}{1.5} & 2 & \color{red}{4} & \color{red}{7} & 8 & 10 & 12 \\
\end{array}
$$

We have two cross over points. Your algorithm may output either $i=0$ or $i=3$.

Design an algorithm to find an index $i \in \{ 0, 1, \ldots, n-1\}$ such that $x_i \geq y_i$ but $x_{i+1} < y_{i+1}$.

Describe your algorithm using python code for a function _findCrossoverIndexHelper(x, y, left, right)_

- `x` is a list of x values sorted in increasing order.
- `y` is a list of y values sorted in increasing order.
- `x` and `y` are lists of same size (`n`).
- `left` and `right` are indices that represent the current search region in the list such that 0 <= `left` < `right` <= `n`

The solution must use _recursion_.
