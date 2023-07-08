def encryption(s):
    # Write your code here
    n = math.ceil(math.sqrt(len(s)))
    
    word = ""
    
    for i in range (n): 
        word += s[i: :n] + " "
            
    return word
