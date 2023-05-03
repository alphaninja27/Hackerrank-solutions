def insertionSort(a):
    # Write your code here
    shift =0
    if len(a) > 1:
        n = len(a)
        leftarr = a[:n // 2]
        rightarr = a[n // 2:]
        shift+=insertionSort(leftarr)
        shift+=insertionSort(rightarr)
        lenl = len(leftarr)
        lenr = len(rightarr)
        i = j =  k = 0
        while (i < lenl and j < lenr):
            if (leftarr[i] <= rightarr[j]):  # <= less shift
                a[k] = leftarr[i]
                i += 1
            else:
                shift += lenl - i
                a[k] = rightarr[j]
                j += 1
            k += 1

        while (i < lenl):
            a[k] = leftarr[i]
            i += 1
            k += 1
        while (j < lenr):
            a[k] = rightarr[j]
            j += 1
            k += 1
    return shift
