def minimumDistances(a):
    # Write your code here
    n = len(a)
    val = []
    for i in range(n-1):    
        for j in range(i+1,n):
            if a[i] == a[j]:
                val.append(j-i)
    if len(val) == 0:
        return -1
    else:
        return min(val)
