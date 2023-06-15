def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()
    res = 0
    maxdist = 0
    dist = k
    for i in range(len(x) - 1):
        if x[i] <= maxdist:
            continue
        else:
            if x[i + 1] <= x[i] + dist:
                dist = x[i] + dist - x[i + 1]
            else:
                res += 1
                dist = k
                maxdist = x[i] + k
    if x[-1] > maxdist:
        res += 1
    return res
