def larrysArray(A):
    # Write your code here
    inversions = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                inversions += 1

    # If the number of inversions is odd, the array cannot be sorted
    if inversions % 2 == 1:
        return "NO"

    # If the number of inversions is even, the array can be sorted
    return "YES"
