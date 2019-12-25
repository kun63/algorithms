def mergesorted(a, b):
    if a == [] or b == []:
        return a+b
    elif a[0] <= b[0]:
        return [a[0]] + mergesorted(a[1:], b)
    else:
        return [b[0]] + mergesorted(a, b[1:])

def mergesort(lst):
    l = len(lst)
    if l <= 1:
        return lst
    return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))

if __name__ == "__main__":
    import sys, time
    sys.setrecursionlimit(100000)
    n = 1000
    while n <= 16000:
        a = list(range(n))
        t = time.time()
        mergesort(a)
        print(n, time.time() - t)
        n *= 2
