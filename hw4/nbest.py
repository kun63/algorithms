from random import *
import heapq


def nbesta(a, b):
    c = [(x,y) for x in a for y in b]
    c.sort(key = t_key)
    return c[:len(a)]

def nbestb(a, b):
    c = [(x,y) for x in a for y in b]
    return res





