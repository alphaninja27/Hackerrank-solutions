def counterGame(n):
    # Write your code here
    if n == 1:
        return 'Richard'
    no_of_plays = 0
    
    while n != 1:
        if math.floor(math.log2(n)) == math.ceil(math.log2(n)):
            n //= 2
        else:
            lowest_power = math.floor(math.log2(n))
            n -= pow(2,lowest_power)
        no_of_plays +=1
    
    if no_of_plays % 2 == 0:
        return 'Richard'
    else:
        return 'Louise'
