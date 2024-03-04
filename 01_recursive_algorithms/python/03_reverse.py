def reverse(arr):
    if len(arr) < 2: return arr
    return [arr[-1]] + reverse(arr[1:-1]) + [arr[0]]
