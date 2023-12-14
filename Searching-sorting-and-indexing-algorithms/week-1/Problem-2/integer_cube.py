def integerCubeRootHelper(n, left, right):
    cube = lambda x: x * x * x # anonymous function to cube a number
    assert(n >= 1)
    assert(left < right)
    assert(left >= 0)
    assert(right < n)
    assert(cube(left) < n), f'{left}, {right}'
    assert(cube(right) > n), f'{left}, {right}'

    while left < right:
        mid = (left + right)//2
        if cube(mid) <= n and cube(mid+1) > n:
            return mid;
        elif cube(mid) < n:
            left = mid + 1
        else:
            right = mid -1
    return left

def integerCubeRoot(n):
    assert( n > 0)
    if (n == 1): 
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)