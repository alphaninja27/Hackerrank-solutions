def maximumToys(prices, k):
    # Write your code here
    prices = sorted(prices)
    toys = 0
    for i in prices:
        if i <= k:
            k = k - i
            toys = toys + 1
        else:
            break
    return toys
