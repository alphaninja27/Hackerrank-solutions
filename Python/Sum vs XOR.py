def sumXor(n):
    # Write your code here
    num_of_zero = 0
    while n != 0 :
        if n % 2 == 0 :
            num_of_zero += 1
        n = n // 2
    return pow(2,num_of_zero)
