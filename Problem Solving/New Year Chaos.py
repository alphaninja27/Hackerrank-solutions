def minimumBribes(q):
    # Write your code here
    bribes = 0
    ori = [x for x in range(1,len(q)+1)]
    i = 0
    while i < len(q):
        if ori[i] == q[i]:
            next
        elif q[i] == ori[i+1]:
            ori[i+1], ori[i] = ori[i], ori[i+1]
            bribes +=1
        elif q[i] == ori[i+2]:
            ori[i+2], ori[i+1] = ori[i+1], ori[i+2]
            ori[i+1], ori[i] = ori[i], ori[i+1]
            bribes +=2
        else:
            print("Too chaotic")
            return
        i+=1
    print(bribes)
    return
