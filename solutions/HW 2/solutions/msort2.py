def mergesort(lst):
    l = len(lst)
    if l <= 1:
        return lst
    return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))

def mergesorted(a, b):
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la or j < lb:
        if i == la or (j != lb and a[i] > b[j]):
            yield b[j]
            j += 1
        else:
            yield a[i]
            i += 1

if __name__ == "__main__":
    import sys, time
    sys.setrecursionlimit(100000)
    n = 1000
    while n <= 128000:
        a = list(range(n))
        t = time.time()
        mergesort(a)
        print(n, time.time() - t)
        n *= 2
