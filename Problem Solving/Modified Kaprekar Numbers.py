def kaprekarNumbers(p, q):
    # Write your code here
    if not [print(n, end=" ") for n in range(p, q + 1) if (int(str(n*n)[:-len(str(n))] or 0) + int(str(n*n)[-len(str(n)):])) == n]: print("INVALID RANGE")
