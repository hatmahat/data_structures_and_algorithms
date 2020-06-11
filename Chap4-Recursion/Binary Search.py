def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False            # kondisi akhir
    else:                               # interval is empty; no match
        mid = (low + high) // 2
        if target == mid:                # found a match
            return True         # kondisi akhir
        elif target < mid:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)      # pengulangan sampai kondisi akhir tercapai
        else:
            return binary_search(data, target, mid + 1, high)   # pengulangan sampai kondisi akhir tercapai

# TESTING
arr = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

print(binary_search(arr, 2, arr[0], arr[-1]))
