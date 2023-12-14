def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that 
    #         left <= i <= right
    #         x[i] <= y[i]
    # Invariants and assertions
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(left <= right-1)
    assert(right < len(x))
    # key property to maintain throughout the algorithm
    assert(x[left] > y[left])
    assert(x[right] < y[right])
    for i in range(left, right):
        if x[i] >= y[i] and y[i+1] >= x[i+1]:
            return i
        
    return -1

def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2
    
    return findCrossoverIndexHelper(x, y, 0, n-1)