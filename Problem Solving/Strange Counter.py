def strangeCounter(t):
    # Write your code here
    cycle = 3
    total = 3
    while total < t:
        cycle *= 2
        total += cycle
    return total - t + 1
