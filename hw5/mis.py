
def max_wis(a, wis=None):
    if a == []:
        return (0,[])
    if wis is None:
        if a[0]>0:
            wis = {0:(0,[]), 1:(a[0],[a[0]])}
        else:
            wis = {0:(0,[]), 1:(0,[])}
    if len(a) in wis:
        return wis[len(a)]
    else:
        #print(max_wis(a[:len(a)-2], wis))
        #print(max_wis(a[:len(a)-1], wis))
        if max_wis(a[:len(a)-2], wis)[0]+a[len(a)-1] > max_wis(a[:len(a)-1], wis)[0]:
            #path=max_wis(a[:len(a)-2], wis)[1]
            #path.append(a[len(a)-1])
            wis[len(a)] = (max_wis(a[:len(a)-2], wis)[0]+a[len(a)-1], max_wis(a[:len(a)-2], wis)[1]+[a[len(a)-1]])
            #print(wis[len(a)])
        else:
            wis[len(a)] = (max_wis(a[:len(a)-1], wis)[0], max_wis(a[:len(a)-1], wis)[1])
        #wis[len(a)][0]=max(max_wis(a[:len(a)-2], wis)[0]+a[len(a)-1], max_wis(a[:len(a)-1], wis)[0])
        return wis[len(a)]


def max_wis2(a):
    """ result  wis[len(a)]
    j   max_wis(a[:len(a)-2])
    k   max_wis(a[:len(a)-1]) """

    if a == []:
        return (0,[])
    if a[0]>0:
        j, k = (0,[]), (a[0],[a[0]])
    else:
        j, k = (0,[]), (0,[])

    for i, x in enumerate(a[1:]):
        if j[0]+x > k[0]:
            result = (j[0]+x, j[1]+[x])
        else:
            result = (k[0], k[1])
        j, k = k, result

    return result



#print(max_wis2([7,8,5]))
#print(max_wis2([-1,8,10]))
#print(max_wis2([-5, -1, -4]))
#print(max_wis([40,-10,45,100]))

#print(max_wis([]))

#print(max_wis([63229, 7871, 74587, 59445, 71381, 5404, 56721, 41863, 62960, 42424, 37376, 38654, 9686, 88564, 71093, 69118, 26876, 44293, 48730, 2476, 58586, 23466, 4192, 48799, 15818, 28847, 82565, 71941, 95094, 64294, 79614, 16219, 16348, 37528, 57940, 73917, 31890, 80693, 88456, 82255, 39260, 8070, 36726, 87408, 44400, 85485, 88349, 45095, 66399, 12786, 99639, 19331, 63101, 72119, 20801, 69561, 33307, 66400, 9388, 41212, 63564, 85236, 72617, 4787, 97918, 32153, 58247, 8466, 68896, 93322, 21028, 18211, 55043, 24187, 13768, 17505, 54214, 71736, 5284, 41499, 87421, 42354, 64137, 77183, 31897, 40971, 94056, 85477, 17893, 95807, 77428, 13186, 51169, 48753, 36957, 27003, 78557, 93281, 84281, 99236]))