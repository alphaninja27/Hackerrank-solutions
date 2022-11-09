def theGreatXor(x):
    # Write your code here
    return (2**(len(bin(x))-2)-1)^x
