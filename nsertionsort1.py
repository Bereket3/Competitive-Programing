def insertionSort1(n, arr):
    # Write your code here
    pevot = arr[len(arr)-1]
    b = n-1
    while b > 0 and pevot<arr[b-1]:
        arr[b]=arr[b-1]
        print(*arr)
        b-=1
    if b == -1: arr[0] = pevot
    else: arr[b] = pevot
    print(*arr)
