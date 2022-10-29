def sansaXor(arr):
    # Write your code here
    if len(arr)%2 == 0:
        return 0
    else:
        xor = 0
        for index in range(0,len(arr),2):
            xor ^=arr[index]
        return xor 
