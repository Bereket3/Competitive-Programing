def countingSort(arr):
    # Write your code here
    out_put = [0 for i in range(100)]
    for i in arr:out_put[i] += 1
    return out_put
