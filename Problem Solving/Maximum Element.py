def getMax(operations):
    # Write your code here
    nums = []
    for x in operations:
        nums.append(x.split())
    st = [0]
    op = []
    for x in nums:
        if int(x[0]) == 1:
            y = int(x[1])
            st.append(max(y,st[-1]))
        elif int(x[0])==2:
            if st:
                st.pop()
        else:
            op.append(st[-1])
    return op
