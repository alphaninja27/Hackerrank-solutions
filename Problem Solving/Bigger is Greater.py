def biggerIsGreater(w):
    # Write your code here
    size=len(w)
    w=list(w)#string to list conversion
    
    for i in range(size-1,0,-1):
        if w[i-1]<w[i]:
            j=i
            while j<size and w[i-1]<w[j]:
                j=j+1
            temp=w[i-1]
            w[i-1]=w[j-1]
            w[j-1]=temp
            w[i:]=reversed(w[i:])
            break
    else:
        return "no answer"
    w="".join(w)
    return w
