def mod_string_1(items,a,i):
    count=0
    index=0
    for _, _, c_i in items:
        count += c_i
        if i <= count:
            a[index]+=1
            break
        else:
            index+=1
    
    return a


def best(W, items, new_items=None, opt=None, N=None):
    if opt == None:
        new_items=[]
        for w_i, v_i, c_i in items:
            if c_i == 1:
                new_items.append((w_i,v_i))
            elif c_i > 1:
                for _ in range(c_i):
                    new_items.append((w_i,v_i))
        opt = {0:{0:(0,[])}}
        path = []
        for i in items:
            path.append(0)
        for n in range(1,len(new_items)+1):
            opt[n]={0:(0,[])}
            for i in range(min([x for x, _ in new_items[:n]])):
                opt[n][i] = (0,path[:])
        for i in range(W+1):
            opt[0][i]=(0,path[:])
        N=len(new_items)



    if W in opt[N]:
        return opt[N][W]
    else:
        
        if new_items[N-1][0]>W:
            next_2=best(W, items, new_items, opt, N-1)
            opt[N][W]=(next_2[0],next_2[1][:])
        else:
            next_1=best(W-new_items[N-1][0], items, new_items, opt, N-1)
            next_2=best(W, items, new_items, opt, N-1)
            opt[N][W]=max((next_1[0]+new_items[N-1][1],mod_string_1(items,next_1[1][:],N)),(next_2[0],next_2[1][:]))

        return opt[N][W]


# print(best(3, [(2, 4, 2), (3, 5, 3)]))
# print(best(3, [(1, 5, 2), (1, 5, 3)]))
# print(best(3, [(1, 5, 1), (1, 5, 3)]))

# print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
# print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))

