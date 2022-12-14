
""" Array indexing
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array,
a[start:stop:step] # start through not past stop, by step. stop value represents the first value that is not in the selected slice
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
a[start:stop:step] is equivalent to a[slice(start, stop, step)]
a[start:] is equivalent to a[slice(start, None)] 
a[::-1] is equivalent to a[slice(None, None, -1)]
"""

def distinct(arr): return list(set(arr))

def binary_search(sorted_list, key, imin, imax):
    if (imax < imin):
        return -1
    imid = (imax + imin) // 2
    if sorted_list[imid] > key: # key is in lower subset
        return binary_search(sorted_list, key, imin, imid - 1)
    elif sorted_list[imid] < key: # key is in upper subset
        return binary_search(sorted_list, key, imid + 1, imax)
    else: # key has been found
        return imid

def binary_search_integer():
    pass

        