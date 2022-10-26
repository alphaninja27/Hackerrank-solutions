def flippingBits(n):
    # Write your code here
    a = '{:032b}'.format(n)
    a = a.replace("0","*").replace("1","0").replace("*","1")
    return(int(a,2))
