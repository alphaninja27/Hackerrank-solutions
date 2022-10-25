def maximizingXor(l, r):
    # Write your code here
    ans = []
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            ans.append(i ^ j)
    return max(ans)
