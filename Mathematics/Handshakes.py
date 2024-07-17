def handshake(n):
    # Write your code here
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return n*(n - 1) // 2
