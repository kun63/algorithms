def sort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        left = [x for x in array if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def sorted(tree):
    if tree == None:
        return None
    return _sorted(tree)

def _sorted(tree):
    if tree == []:
        return []
    return sorted(tree[0]) + [tree[1]] + sorted(tree[2])

def search(tree, x):
    if tree == None:
        return False
    position = _search(tree, x)
    return position != []

def insert(tree, x):
    if tree == None:
        return
    position = _search(tree, x)
    if position != []:
        return
    position.extend([[],x,[]])

def _search(tree, x):
    if tree == [] or x == tree[1]:
        return tree
    elif x > tree[1]:
        return _search(tree[2], x)
    elif x < tree[1]:
        return _search(tree[0], x)
