from collections import defaultdict


def longest(n, edges):


    def _longest(n, edges, opt=None):
        
        if n in opt:
            return opt[n]

        result = min([(_longest(i, edges, opt)-1, i) for i in adj_edges[n]])
        back[n]=result[1]

        opt[n] = result[0]


        return opt[n]



    adj_edges = defaultdict(list)
    adj_edges_2 = defaultdict(list)
    for e in edges:
        adj_edges[e[1]].append(e[0])
        adj_edges_2[e[0]].append(e[1])
    

    end_node = []
    head_node = []
    back = [0]*n
    for i in range(n):
        if i not in adj_edges and i in adj_edges_2:
            head_node.append(i)
        if i not in adj_edges_2 and i in adj_edges:
            end_node.append(i)
    opt = {}
    for h in head_node:
        opt[h] = 0

    if edges == []:
        return 0, []
    result = min([(_longest(x, edges, opt), x) for x in end_node])
    max_v = result[1]
    result = result[0]


    v = max_v
    _back = [v]
    while v != 0:
        v = back[v]
        _back[:0] = [v]
    

    return -result, _back

    
if __name__ == "__main__":
    print(longest(15, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (5,6), (4,5), (5,7),(9,10), (10, 11)]))
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
    print(longest(1000, []))
    # print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))