def find(a):
    a.sort()
    output=[]
    for p, x in enumerate(a[2:]):
        i, j = 0, p+1
        while i<j:
            if a[i]+a[j]==x:
                output.append((a[i], a[j], a[i]+a[j]))
                i += 1
            elif a[i]+a[j]<x:
                i += 1
            else:
                j -= 1
    return output

print(find([1, 4, 2, 3, 5]))
