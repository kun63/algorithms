def find(A, x, k):
    
    i=0
    index=list(range(0,k))
    index_value=[A[i]-x for i in range(0, k)]
    for i, v in enumerate(index_value):
        if v < 0:
            index_value[i]=-v
    for i in range(len(A)-k,len(A)):
        t=A[i]-x
        if t < 0:
            t = -t
        for j, v in enumerate(index_value):
            if t < v:
                v = t
                index[j]=i
                break
    output=[]
    for i in index:
        output.append(A[i])
    return output

print(find([4,1,3,2,7,4], 6.5, 3))