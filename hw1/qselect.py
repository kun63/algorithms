from random import randint
def qselect(k,a):
    if a == []:
        return []
    index = randint(0,len(a)-1)
    a[0], a[index] = a[index], a[0]
    pivot =  a[0]
    #pivot = a[0]
    left = [x for x in a if x < pivot]
    
    if len(left) == k-1:
        return pivot
    elif len(left) > k-1:
        return qselect(k,left)
    else:
        #right =  [x for x in a[1:] if x >= pivot]
        right = [x for x in a[1:] if x >= pivot]
        return qselect(k-len(left)-1,right)

#print(qselect(4, [11, 2, 8, 3]))
#print(qselect(2, [3, 10, 4, 7, 19]))

