def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        x = arr[0]
        arr.remove(arr[0])
        arr.append(x)
    return arr
