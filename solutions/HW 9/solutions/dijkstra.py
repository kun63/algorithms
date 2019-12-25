__author__ = "liang huang"

# two version: heapdict (decrease_key) or heapq (duplicates in heap)
from heapdict import heapdict 
from collections import defaultdict
from heapq import heappush, heappop

# O((V+E) log V) -- using heapdict and decrease_key
def shortest(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges:
        edges[u].append((v, cost))
        edges[v].append((u, cost))
    h = heapdict() 
    h[0] = 0 # alternatively, you can also set everything else to +inf
    back = {}
    popped = set() # those already popped (i.e., black nodes)
    while h: #len(h) > 0:
        v, d = h.popitem()
        popped.add(v)
        if v == n-1: # target is popped (fixed)
            return d, solution(v, back)
        for (u, cost) in edges[v]:
            if u not in popped: # N.B.: important check
                newd = d + cost
                if u not in h or newd < h[u]: # forward update;
                    h[u] = newd # automatic decrease-key()
                    back[u] = v 
    return None # target is not reachable

# O((E+E) log E) -- using heapq, duplicates in heap
def shortest_heapq(n, _edges):
    edges = defaultdict(list)
    for (u, v, cost) in _edges:
        edges[u].append((v, cost))
        edges[v].append((u, cost))
    h = [(0, 0, None)] # (value, node, back_ptr)
    back = {} # (fixed) backptrs for those already popped (i.e., black nodes)
    while h: #len(h) > 0:
        d, v, u = heappop(h)
        if v not in back:
            back[v] = u
            if v == n-1: # target is popped (fixed)
                return d, solution(v, back)
            for (u, cost) in edges[v]:
                if u not in back: # N.B.: important check
                    newd = d + cost
                    heappush(h, (newd, u, v)) # automatic decrease-key()
    return None # target is not reachable

# shortest = shortest_heapq # use heapq version

def solution(v, back):
    if v == 0:
        return [0]
    return solution(back[v], back) + [v]

if __name__ == "__main__":
    print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])) # unreachable

    def generate_seq(k,length,seed): 
        import random; random.seed(seed); return [tuple(sorted(random.sample(range(k),2))+[random.randint(5,10)]) for _ in range(length)]

    dense = generate_seq(1000, 5000, 1)
    print(shortest(1000, dense)) # (25, [0, 331, 301, 728, 999])
    print(shortest(1000, [(0, 89, 10), (0, 221, 5), (0, 301, 20), (0, 331, 5), (0, 404, 16), (0, 728, 21), (0, 999, 27), (89, 728, 11), (89, 999, 16), (221, 382, 5), (221, 331, 5), (301, 331, 7), (301, 728, 8), (301, 999, 15), (331, 404, 7), (331, 473, 8), (331, 496, 10), (332, 534, 10), (331, 999, 30), (728, 996, 9), (996, 999, 5), (728, 999, 5)]))
    
    print(shortest(8, [(0,4,2), (0,1,7), (0,7,12), (1,2,1), (1,3,1), (1,7,5), (2,3,3), (2,4,1), (2,5,1), (2,7,10), (3,6,2), (3,4,5), (3,7,1)]))
