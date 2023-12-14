## Problem 3 (Develop Multiway Merge Algorithm, 15 points).

We studied the problem of merging 2 sorted lists `lst1` and `lst2` into a single sorted list in time $\Theta(m + n)$ where $m$ is the size of `lst1` and $n$ is the size of `lst2`. Let `twoWayMerge(lst1, lst2)` represent the python function that returns the merged result using the approach presented in class.

In this problem, we will explore algorithms for merging `k` different sorted lists, usually represented as a list of sorted lists into a single list.

Suppose we have $k$ lists that we will represent as `lists[0]`, `lists[1]`, ..., `lists[k-1]` for convenience and the size of these lists are all assumed to be the same value $n$.

We wish to solve multiway merge by merging two lists at a time:

```
  mergedList = lists[0] # start with list 0
  for i = 1, ... k-1 do
      mergedList = twoWayMerge(mergedList, lists[i])
  return mergedList
```

Implement an algorithm that will implement the $k$ way merge by calling `twoWayMerge` repeatedly as follows:

1. Call `twoWayMerge` on consecutive pairs of lists `twoWayMerge(lists[0], lists[1])`, ... , `twoWayMerge(lists[k-2], lists[k-1])` (assume k is even).
2. Thus, we create a new list of lists of size `k/2`.
3. Repeat steps 1, 2 until we have a single list left.
