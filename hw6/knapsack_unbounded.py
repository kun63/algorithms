def transfer_string(a,i):
    a[i]+=1
    return a

def best(W, items, opt=None):
    if opt == None:
        opt = {0:(0,[])}
        path = []
        for i in items:
            path.append(0)
        for i in range(min([x for x, _ in items])):
            opt[i] = (0,path[:])
        
    if W in opt:
        return opt[W]
    else:
        opt[W] = max([(best(W-w_i, items, opt)[0]+v_i, transfer_string(best(W-w_i, items, opt)[1][:],i)) for i, (w_i, v_i) in list(enumerate(items)) if w_i <= W])
        return opt[W]
