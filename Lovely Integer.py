def lonelyinteger(a):
    # Write your code here
    for i in a:
        if a.count(i) == 1:
            return i
