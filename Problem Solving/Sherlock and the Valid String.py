def isValid(s):
    # Write your code here
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    print(d)
    ans = list(d.values())
    adj = False
    freq = max(set(ans), key = ans.count)
    for v in ans:
        if v != freq:
            if adj:
                return 'NO'
            if abs(freq - v) == 1:
                adj = True
            if abs(v - freq) > 1:
                if v == 1:
                    continue
                else:
                    return 'NO'
    return 'YES'
