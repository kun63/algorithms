#!/usr/bin/env python

import bisect

def find(a, x, k):
    assert k <= len(a), "k shouldn't be larger than n!"
    a = [float("-inf")] + a + [float("inf")]
    place = bisect.bisect(a, x)
    i, j = place-1, place
    for _ in range(k):
        if x-a[i] <= a[j]-x:
            i -= 1
        else:
            j += 1
    return a[i+1:j]

if __name__ == "__main__":
   print(find([1,2,3,4,4,7], 5.2, 2)) #   [4,4]
   print(find([1,2,3,4,4,7], 6.5, 3)) #   [4,4,7]
   print(find([1,2,3,4,4,6,6], 5, 3)) #   [4,4,6]
   print(find([1,2,3,4,4,5,6], 4, 5)) #   [2,3,4,4,5]
   print(find([1], 4, 1)) # [1]
   print(find([1], 1, 1)) # [1]
   print(find([1,1,1], 1, 2)) # [1,1]
   print(find([1], 4, 2)) # NOT ALLOWED k <= n
