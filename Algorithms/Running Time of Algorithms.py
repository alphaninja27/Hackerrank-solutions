def runningTime(arr):
    # Write your code here
    res = 0
    for i in range(1, len(arr)):
        j = i - 1
        k = arr[i]
        
        while arr[j] > k and j>=0:
            arr[j+1] = arr[j]
            j-=1
            res += 1
        arr[j+1] = k
        
    return res
