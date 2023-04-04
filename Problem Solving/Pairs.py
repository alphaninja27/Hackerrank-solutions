def pairs(k, arr):
    # Write your code here
    return len(set(arr).intersection(set(x+k for x in arr)))
