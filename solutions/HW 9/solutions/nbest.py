from heapq import heappush, heappop, heapify

def nbest(ABs):    # no need to pass in k or n
    k = len(ABs)
    n = len(ABs[0][0])
    
    def trypush(i, p, q):  # push pair (A_i,p, B_i,q) if possible
        A, B = ABs[i] # A_i, B_i
        if p < n and q < n and not (i,p,q) in used:
            heappush(h, ((A[p]+B[q],A[p]), i, p, q, (A[p],B[q])))
            used.add((i, p, q))

    h, used = [], set()                   # initialize
    # for i in range(k): # slow version
    #     trypush(i, 0, 0)
    h = [((A[0]+B[0], A[0]), i, 0, 0, (A[0],B[0])) for i, (A,B) in enumerate(ABs)] # fast version
    heapify(h)
    for _ in range(n):
        _, i, p, q, pair = heappop(h)
        yield pair     # return the next pair (in a lazy list)
        trypush(i, p, q+1)
        trypush(i, p+1, q)

if __name__ == "__main__":
    
    print(list(nbest([([1,2,4], [2,3,5]), ([0,2,4], [3,4,5])]))) # == [(0, 3), (1, 2), (0, 4)]

    print(list(nbest([([-1,2],[1,4]), ([0,2],[3,4]), ([0,1],[4,6]), ([-1,2],[1,5])]))) # == [(-1, 1), (-1, 1)]

    print(list(nbest([([5,6,10,14],[3,5,10,14]),([2,7,9,11],[3,8,12,16]),([1,3,8,10],[5,9,10,11]),([1,2,3,5],[3,4,9,10]),([4,5,9,10],[2,4,6,11]),([4,6,10,13],[2,3,5,9]),([3,7,10,12],[1,2,5,10]),([5,9,14,15],[4,8,13,14])])))     #[(1, 3), (3, 1), (1, 4), (2, 3)]

    print(list(nbest([([1,6,8,13],[5,8,11,12]),([1,2,3,5],[5,9,11,13]),([3,5,7,10],[4,6,7,11]),([1,4,7,8],[4,9,11,15]),([4,8,10,13],[4,6,10,11]),([4,8,12,15],[5,10,11,13]),([2,3,4,8],[4,7,11,15]),([4,5,10,15],[5,6,7,8])])))   #[(1, 4), (1, 5), (1, 5), (2, 4)]

