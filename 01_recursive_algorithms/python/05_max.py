def findMax(arr):
    if len(arr) == 0: raise Exception("invalid argument")
    if len(arr) == 1: return arr[0]
    return max(arr[0], findMax(arr[1:]))
