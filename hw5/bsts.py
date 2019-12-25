def bsts(n, bsts_result=None):
    if bsts_result is None:
        bsts_result = {0:1, 1:1}
    if n in bsts_result:
        return bsts_result[n]
    else:
        result=0
        for i in range(n):
            result += bsts(i, bsts_result) * bsts(n-i-1, bsts_result)
    bsts_result[n]=result
    return result
