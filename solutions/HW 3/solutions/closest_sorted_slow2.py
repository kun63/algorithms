#!/usr/bin/env python
import bisect
import random
random.seed(10)

def find(l,p,n):
    split = bisect.bisect(l,p)
    left, right = [float('-inf')]+l[:split], l[split:]+[float('inf')]
    goal = []
    for i in range(n):
        goal = [left.pop()]+goal if abs(left[-1]-p) <= abs(right[0]-p) else goal+[right.pop(0)]
    return goal


if __name__ == "__main__":
    ### random generate some test cases
    l = [random.randint(0,100) for r in range(20)]
    l.sort()
    pivot = random.randint(0,100)
    size = random.randint(4,8)
    print(l, pivot,size)
    print(find(l,pivot,size)) 
    ### given test case
    print(find([1,2,3,4,4,6,6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))
    print(find([1,2,3,4,4,7], 5.2, 2))
    print(find([1,2,3,4,4,7], 6.5, 3))
    
