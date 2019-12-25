import bisect

def find(a, x, n):
    place = bisect.bisect(a,x)
    i, j = place-1, place
    a.append(float("inf"))
    for _ in range(n):
        if x-a[i]<=a[j]-x:
            i -= 1
        else:
            j += 1
    output=[]
    for k in range(i+1,j):
        output.append(a[k])
    return output

