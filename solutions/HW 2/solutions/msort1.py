def mergesort(lst):
    l = len(lst)
    if l <= 1:
        return lst
    return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))

def mergesorted(a, b):
    if a == [] or b == []:
        return a+b
    c = []
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la or j < lb:
        if i == la or (j != lb and a[i] > b[j]):
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    return c

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
