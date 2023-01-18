def candies(n, arr):
    # Write your code here
    candies = [1 for x in range(0, n)]
    
    for c in range(1, n):
        if arr[c] > arr[c-1]:
            candies[c] = candies[c-1] + 1
    for b in range(n-2, -1, -1):
        if arr[b] > arr[b+1]:
            candies[b] = max(candies[b+1] + 1, candies[b])
        
    print(candies)
    return sum(candies)
