import heapq
import math

def kmergesort(a,k):
    if a == []:
        return []
    if len(a) == 1:
        return a
    step=math.ceil(len(a)/k)
    #print(step)
    output=[]
    i=0
    temp=[]
    while i+step <= len(a):
        temp=kmergesort(a[i:i+step],k)
        output.append(temp)
        i += step
    if i is not len(a):
        temp=kmergesort(a[i:len(a)],k)
        output.append(temp)
    return kmerge(output)

    #return kmerge(output)


def kmerge(a):
    #print(a)
    k =  len(a)
    num_list = [x for x in range(k)]
    index_list = [0 for x in range(k)]
    h = [[a[num_list[i]][0], i, index_list[i]] for i in range(k)]
    heapq.heapify(h)
    output = []
    while len(h) is not 0:
        output.append(h[0][0])
        index = h[0][1]
        if index_list[index] < len(a[index])-1:
            index_list[index] += 1
            heapq.heapreplace(h,[a[num_list[index]][index_list[index]], index, index_list[index]])
        else:
            heapq.heappop(h)
    return output

#print(kmergesort([4,1,5], 3))
#print(kmerge([[4], [1], [5]]))
#print(kmergesort([4,1,5,2,6,3,7,0],3))