

def mergesort(arr, inversion = 0):
    if arr == []:
        return [], inversion
    if len(arr) == 1:
        return arr, inversion
    index = int(len(arr) / 2)
    left = mergesort(arr[:index], inversion)
    right = mergesort(arr[index:], inversion)
    inversion = left[1] + right[1]
    return merge(left[0], right[0], inversion)

def merge(left, right, inversion):
    left_len, right_len = len(left), len(right)
    output = []
    i, j = 0, 0
    while i <= left_len - 1 or j <= right_len -1:

        if j == right_len:
            output.append(left[i])
            i += 1
        elif i == left_len:
            output.append(right[j])
            j += 1
        elif left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            inversion += (left_len - i)
            j += 1
    return output, inversion


def num_inversions(arr):
    
    return mergesort(arr)[1]



#print(num_inversions([4, 1, 3, 2]))
#print(num_inversions([2, 4, 1, 3]))


