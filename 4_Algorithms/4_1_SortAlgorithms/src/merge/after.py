def merge_sort(x, low=0, high=-1, arr=None):
    if arr is None:
        arr = [0] * len(x)
    
    if high == -1:
        high = len(x) - 1

    if low >= high:
        return
    
    mid = (low + high) // 2
    merge_sort(x, low, mid, arr)
    merge_sort(x, mid + 1, high, arr)
    
    i, j = low, mid + 1
    for k in range(low, high + 1):
        if j > high:
            arr[k] = x[i]
            i += 1
        elif i > mid:
            arr[k] = x[j]
            j += 1
        elif x[i] <= x[j]:
            arr[k] = x[i]
            i += 1
        else:
            arr[k] = x[j]
            j += 1
    
    x[low:high + 1] = arr[low:high + 1]