def beautifulTriplets(d, arr):
    # Write your code here
    arr = sorted(arr)
    n = len(arr)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            dij = arr[j] - arr[i]
            if dij > d:
                break
            if dij == d:
                for k in range(j + 1, n):
                    djk = arr[k] - arr[j]
                    if djk == d:
                        count += 1
                    if djk > d:
                        break
    return count
