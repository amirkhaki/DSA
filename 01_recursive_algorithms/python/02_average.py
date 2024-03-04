def average(arr, n, sum_so_far = 0):
    if len(arr) == 0:
        return sum_so_far / n
    return average(arr[1:], n, sum_so_far + arr[0])

print(average([1,2,3,4,5], 5, 0))
