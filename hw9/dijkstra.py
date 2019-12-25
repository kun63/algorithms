from heapdict import heapdict
from collections import defaultdict

def shortest(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    stack = heapdict()
    stack[0] = 0
    visited = set()
    back = [0]*n
    back[0] = -1
    path = []
    while len(stack) != 0:
        u, d = stack.popitem()
        visited.add(u)
        if u == n-1:
            temp = n-1
            while temp != -1:
                path[:0] = [temp]
                temp = back[temp]
            # print(back)
            return d, path
        for v, w in graph[u]:
            if v in visited:
                continue
            elif v in stack:
                if stack[v] > d+w:
                    stack[v] = d+w
                    back[v] = u
                # stack[v] = min(stack[v], d+w)
            else:
                stack[v] = d+w
                back[v] = u

    return None







if __name__ == "__main__":
    print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print(shortest(4, [(0,1,1), (2,3,1)]))
    print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))