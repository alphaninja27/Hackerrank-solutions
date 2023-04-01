def balancedSums(arr):
    # Write your code here
    l,r = 0, sum(arr)
    if l == r:
        return 'YES'
    else:
        r -= arr[0]
    if l == r:
        return 'YES'
    for i in range(1,len(arr)):
        l += arr[i - 1]
        r -= arr[i]
        if l == r:
            return 'YES'
    return "NO"
