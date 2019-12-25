#!/usr/bin/env python3

from collections import defaultdict

def _order(n, edges): # using stack
   
    # convert list of edges to adj. list
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in edges: # u->v
        adjlist[u].append(v)
        indegree[v] += 1
        
    print(adjlist)
    print(indegree)

    stack = []
    for u in range(n): # nodes are 0..(n-1)
        if indegree[u] == 0:
            stack.append(u)
    while stack != []:
        u = stack.pop() 
        yield u # next in the topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)

def _order2(n, edges): # using queue
   
    # convert list of edges to adj. list
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in edges: # u->v
        adjlist[u].append(v)
        indegree[v] += 1
        
    print(adjlist)
    print(indegree)

    queue = []
    for u in range(n): # nodes are 0..(n-1)
        if indegree[u] == 0:
            queue.append(u)
    head = 0
    while head < len(queue):
        u = queue[head] # pop queue
        head += 1
        yield u # next in the topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

order = lambda n, edges: list(_order2(n, edges))

if __name__ == "__main__":
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])) #  == [0, 1, 2, 4, 3, 5, 6, 7])


