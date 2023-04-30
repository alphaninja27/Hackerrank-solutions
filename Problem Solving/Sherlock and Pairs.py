def solve(a):
    # Write your code here
    C = Counter(a)
    return sum(n*(n-1) for n in C.values())
