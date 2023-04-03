def missingNumbers(arr, brr):
    # Write your code here
    for element in arr: 
        brr.remove(element)
    return sorted(set(brr))
    
