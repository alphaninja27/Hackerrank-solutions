def connectedCell(matrix):
    # Write your code here
    I,J  = len(matrix), len(matrix[0])
    dirs = (0,-1), (-1,-1), (-1,0), (-1,1)
    reg = [None]
    size = [0]
    def top(r):
        while reg[r] != r: r=reg[r]
        return r

    for i, line in enumerate(matrix):
        for j,v in enumerate(line):
            if v:
                see = set(top(matrix[i+di][j+dj])
                        for di,dj in dirs
                        if 0<=i+di<I and 0<=j+dj<J
                          and matrix[i+di][j+dj] > 0
                    )
                if see:
                   rno = max(see)
                   matrix[i][j] = rno
                   size[rno] += 1
                   for sno in see:
                       if sno != rno:
                           reg[sno] = rno
                           size[rno] += size[sno]
                else:
                    rno = len(reg)
                    reg.append(rno)
                    size.append(1)
                    matrix[i][j] = rno
    return max(size)
