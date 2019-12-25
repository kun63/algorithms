__author__ = "liang huang"

'''easy-to-understand version'''

from heapq import heapify, heappop, heappush
from collections import defaultdict
allowed = set(['AU','UA','CG','GC','GU','UG']) # this should be set, not list

def best(s): # using overlapping formulation

    def update(i, j, value, trace):
        if value > opt[i, j]:
            opt[i, j] = value
            back[i, j] = trace
    
    def solution(i, j):
        if i == j: # singleton
            return "."
        elif j == i-1: # empty
            return ""
        t = back[i, j]
        if t == -1: # pair
            return "(%s)" % solution(i+1, j-1) 
        return "%s%s" % (solution(i, t), solution(t+1, j)) # split

    n = len(s)
    opt = defaultdict(lambda : -1)
    back = {}
    for i in range(n):
        opt[i, i-1] = 0
        opt[i, i] = 0

    for span in range(2, n+1): # span length: 2..n
        for i in range(n-span+1): # left boundary: 0..(n-span)
            j = i+span-1 # right boundary
            
            if s[i]+s[j] in allowed: # pair (___)
                update(i, j, opt[i+1, j-1] + 1, -1)
            for k in range(i, j): # split point: i..j-1
                update(i, j, opt[i, k] + opt[k+1, j], k)
            
    return opt[0, n-1], solution(0, n-1)

def total(s): # using KT formulation

    ''' tot[i,j] -- total; pair[i,j] -- subset of total with i--(j-1): (xxxx)'''

    n = len(s)
    tot = defaultdict(int)

    for i in range(n+1): # NB
        tot[i, i+1] = 1 # singleton .
        tot[i, i] = 1 # empty

    for span in range(2, n+1): # span length: 2..n
        for i in range(n-span+1): # left boundary: 0..(n-span)
            j = i+span # right boundary
            
            tot[i, j] += tot[i+1, j] # case 1: i unpaired 

            for k in range(i+1, j+1): # split point: i+1..j-1
                if s[i]+s[k-1] in allowed: # pair (___)                    
                    tot[i, j] += tot[i+1, k-1] * tot[k, j] # case 3: i paired with k-1 (k<j)

    return tot[0, n]

def kbest(s, k): # using KT formulation

    def tryadd_binary(split, index1, index2):
        if index1 < len(opt[i, split-1]) and index2 < len(opt[split+1, j-1]) \
           and not (split, index1, index2) in used:
            used.add((split, index1, index2))
            heappush(heap, 
                     (-(opt[i, split-1][index1][0]+opt[split+1, j-1][index2][0] + 1), split, index1, index2))

    def tryadd_unary(index):
        if index < len(opt[i, j-1]):
            heappush(heap, (-opt[i, j-1][index][0], index)) # min-heap

    n = len(s)
    opt = defaultdict(list) # list of (value, structure) pairs
    for i in range(n):
        opt[i, i] = [(0, '.')] # singleton
        opt[i, i-1] = [(0, '')] # empty

    for span in range(2, n+1): # span length: 2..n
        for i in range(n-span+1): # left boundary: 0..(n-span)
            j = i+span-1 # right boundary

            heap = []            
            used = set()

            for m in range(i, j): # try (m,j) pair where m=i..(j-1)
                if s[m]+s[j] in allowed: # pair (___)
                #heap.append((-opt[i+1, j-1][0][0]-1, 0)) # min-heap
                    tryadd_binary(m, 0, 0)
            tryadd_unary(0) # j unpaired

            uniq = set()
            for _ in range(k):
                if heap == []: 
                    break
                item = heappop(heap)
                if len(item) == 2: # j unpaired
                    value, index = item
                    opt[i, j].append((-value, "%s." % opt[i,j-1][index][1])) # check duplicates
                    tryadd_unary(index+1)
                else: # j paired
                    value, split, index1, index2 = item
                    opt[i, j].append((-value, "%s(%s)" % (opt[i, split-1][index1][1],
                                                          opt[split+1, j-1][index2][1])))
                    tryadd_binary(split, index1+1, index2)
                    tryadd_binary(split, index1, index2+1)

    return opt[0,n-1]

print(best("ACAGU"))
print(total("ACAGU"))
print(kbest("ACAGU", 10))
print(kbest("AGGCAUCAAACCCUGCAUGGGAGCG", 10))
