def restaurant(l, b):
    # Write your code here
    if l == b:
        return 1

    maxSize = min(l,b)

# Find greatest common factor
    for size in range(maxSize,0,-1):
        if l%size == 0 and b%size == 0:
            return l*b//(size**2)
