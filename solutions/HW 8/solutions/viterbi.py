__author__ = "liang huang"

from collections import defaultdict

def order(n, edges):

    degrees = defaultdict(lambda : 1) # dummy source -> all v
    for u in edges:
        for v in edges[u]:
            degrees[v] += 1  # count in-degree
    edges[-1] = list(range(n)) # dummy source -> everybody

    current = [-1] # zero-degrees nodes
    front = 0  # queue head pointer
    out = [] # final output order
    while front < len(current):
        v = current[front]
        out.append(v)
        front += 1 # pop queue head
        for u in edges[v]:  # v->u; update u
            degrees[u] -= 1 
            if degrees[u] == 0:
                current.append(u)
    if len(out) == n+1:
        return out[1:] # excluding dummy source
    return None # cycle found

def longest(n, _edges):

    def solution(v): # backtrace
        if v not in back: # no predecessor, end of recursion: start node of the longest path
            return [v]
        return solution(back[v]) + [v]

    edges = defaultdict(list)
    for (u,v) in _edges:
        edges[u].append(v) # make adjacent list from edge list
    for u in range(n):
        edges[u].append(n) # dummy sink (all v -> sink)
        
    best = defaultdict(int)
    back = {}
    for u in order(n+1, edges): # n+1 nodes including dummy sink
        for v in edges[u]: # forward update
            if best[u] + 1 > best[v]: 
                best[v] = best[u] + 1
                back[v] = u

    return best[n]-1, solution(back[n]) # not including dummy sink

if __name__ == "__main__":
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, []))
