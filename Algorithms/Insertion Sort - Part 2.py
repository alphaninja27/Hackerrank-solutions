def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        print(*arr)
