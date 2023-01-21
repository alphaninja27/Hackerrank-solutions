def fibonacciModified(t1, t2, n):
    # Write your code here
    for i in range(n-2):
        t3 = t1 + t2**2
        t1,t2 = t2,t3
    return t2
