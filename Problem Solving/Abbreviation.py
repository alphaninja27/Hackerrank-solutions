def abbreviation(a, b):
    # Write your code here
    dp = [[False for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    dp[0][0] = True
    for i in range(len(a)):
        for j in range(len(b)+1):
            if dp[i][j]:
                if j < len(b) and a[i].upper() == b[j]:
                    dp[i+1][j+1] = True
                if a[i].islower():
                    dp[i+1][j] = True
    return 'YES' if dp[len(a)][len(b)] else 'NO'
