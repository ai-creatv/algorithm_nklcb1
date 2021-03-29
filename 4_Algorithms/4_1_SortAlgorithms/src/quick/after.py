def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    left = []
    right = []
    for a in x:
        if a < pivot:
            left.append(a)
        else:
            right.append(a)

    return quicksort(left) + [pivot] + quicksort(right)