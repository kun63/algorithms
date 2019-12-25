def longest_(arr):
    if arr == []:
        return [-1, 0]
    if arr[0] == [] and arr[2] == []:
        return [0, 0]
    left = longest_(arr[0])
    right = longest_(arr[2])
    
    middle = [0, left[0] + right[0] + 2]
    output = max([left, right, middle], key = lambda a: a[1])
    if output == middle:
        middle[0] = max(left[0], right[0]) + 1
        return middle
    else:
        output[0] += 1
        return output

def longest(arr):
    return longest_(arr)[1]


#print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))