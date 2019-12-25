def order(n, edges):
    entry = {x:0 for x in range(n)}
    for e in edges:
        entry[e[1]] += 1
    q = [x for x in entry if entry[x] == 0]
    path = []
    if q == []:
        return None
    trash = []
    while(q != []):
        q.sort()
        node = q.pop(0)
        path.append(node)
        for e in edges:
            if e[0] == node:
                entry[e[1]] -= 1
                if entry[e[1]] == 0:
                    q.append(e[1])
                #edges.remove(e)
                trash.append(e)
        for e in trash:
            edges.remove(e)
            trash.remove(e)
    
    #print(edges)
    if edges == []:
        return path
    else:
        return None

# print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
# print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
# print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
# print(order(5, [(0,1), (1,2), (2,3), (3,4)]))
# print(order(5, []))
# print(order(3, [(1,2), (2,1)]))
# print(order(1, [(0,0)]))