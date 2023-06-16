def countingSort(arr):
    # Write your code here
    aux = [0]*100
    for i in arr:
        aux[i] += 1
    ans = []
    for i,x in enumerate(aux):
        if x > 0:
            ans += [i]*x
    return ans
