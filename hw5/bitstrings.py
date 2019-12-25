import math

def num_no(n, no_result=None):
    if no_result is None:
        no_result = {0:1, 1:2}
    if n in no_result:
        return no_result[n]
    else:
        return num_no(n-2, no_result) + num_no(n-1, no_result)

def num_yes(n):
    return int(math.pow(2,n)-num_no(n))
