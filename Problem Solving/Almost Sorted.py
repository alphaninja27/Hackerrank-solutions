def almostSorted(arr):
    # Write your code here
    arrr=sorted(arr)
    
    if arr ==arrr:
        return (print("yes"))

    index=[]
    for i in range(len(arr)):
        if arr[i] != arrr[i]:
            index.append(i)

    if len(index)==2:
        temp=arr[index[0]]
        arr[index[0]]=arr[index[1]]
        arr[index[1]]=temp
        if arr == arrr:
            print("yes")
            return (print("swap {} {}".format(index[0]+1,index[1]+1)))
            
    
    elif len(index)>2:
        newarr=arr[:index[0]]+arr[index[-1]:index[0]-1:-1]+arr[index[-1]+1:]
        if newarr==arrr:
            print("yes")
            return (print("reverse {} {}".format(index[0]+1,index[-1]+1)))
            
    return print("no")
