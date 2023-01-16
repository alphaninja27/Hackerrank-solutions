def getWays(n, c):
    # Write your code here
    perms = [1] + [0] * n
    for coin in c:
        for i in range(coin, n + 1):
            perms[i] += perms[i - coin]
    return perms[n]
