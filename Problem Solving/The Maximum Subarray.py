def maxSubarray(arr):
    # Write your code here
    max_sum = 0
    curr_sum = 0
    # checking if all the arr values are negative
    neg_check = True
    neg_check = all([False for i in arr if i > 0])
    # if neg return the max of neg values
    if neg_check:
        return max(arr), max(arr)
    # else find the max value for subarray using Kadane's algo
    for i in arr:
        curr_sum += i
        # for each subarray sum compare it with max sum
        max_sum = max(curr_sum, max_sum)
        # if curr_sum becomes neg, discard that subarray and start fresh
        if curr_sum < 0:
            curr_sum = 0
     # finding max in a subsequence - order of elements need not be conserved   
    sub_seq_sum = sum([i for i in arr if i > 0])
    return max_sum, sub_seq_sum
