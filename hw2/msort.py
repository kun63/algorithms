def mergesort(arr):
    if arr == []:
        return []
    if len(arr) == 1:
        return arr
    index = int(len(arr) / 2)
    return merge(mergesort(arr[:index]), mergesort(arr[index:]))

def merge(left, right):
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
            j += 1
    return output

#print(merge([2, 4], [1, 5]))
print(mergesort([4, 2, 5, 1, 6, 3, 7]))