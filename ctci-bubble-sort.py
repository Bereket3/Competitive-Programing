def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j]>a[j+1]:
                count += 1
                a[j], a[j+1] = a[j+1], a[j]
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[len(a)-1]}')
