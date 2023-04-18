def absolutePermutation(n, k):
    # Write your code here
    if k == 0:
        return list(range(1, n+1))
    elif n % (2*k) != 0:
        return [-1]
    else:
        absolute_permutations = []
        for i in range(1, n//(2*k)+1):
            for j in range(2*k*(i-1)+1, 2*k*i+1):
                if (j-1)//k % 2 == 0:
                    absolute_permutations.append(j+k)
                else:
                    absolute_permutations.append(j-k)
        return absolute_permutations
