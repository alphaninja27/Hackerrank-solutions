def countingSort(arr):
    # Write your code here
    ans = [0] * 100
    for i in arr:
        ans[i] += 1
    return ans
