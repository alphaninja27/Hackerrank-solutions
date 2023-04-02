def icecreamParlor(m, arr):
    # Write your code here
    a = []
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] ==m:
                a.append(i+1)
                a.append(j+1)
                return a
