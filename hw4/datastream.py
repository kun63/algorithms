import heapq

def ksmallest(k,n):
    h=[-x for x in n[0:k]]
    
    heapq.heapify(h)
    #return h
    for t in n[k:]:
        if -h[0]>t:
            heapq.heapreplace(h,-t)

    output=[-x for x in h]
    output.sort()

    return output




#print(ksmallest(3, range(1000000, 0, -1)))