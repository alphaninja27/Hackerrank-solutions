def twoPluses(grid):
    # Write your code here
    plusses=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 'B':
                max_plus_length=min((len(grid)-1)//2, (len(grid[0])-1)//2, i, j, len(grid)-i-1, len(grid[0])-j-1)
                plus = set()
                plus.add((i,j))
                plusses.append(plus)
                for k in range(1, max_plus_length+1):
                    if grid[i-k][j] == 'G' and \
                       grid[i+k][j] == 'G' and \
                       grid[i][j-k] == 'G' and \
                       grid[i][j+k] == 'G':
                        plus.add((i-k,j))
                        plus.add((i+k,j))
                        plus.add((i,j-k))
                        plus.add((i,j+k))
                    else:
                        break
                    subplus = plus.copy()
                    plusses.append(subplus)

    max_area_product = 0
    for pi in plusses:
        for pj in plusses:
            if not pi.intersection(pj):
                max_area_product = max(max_area_product, len(pi)*len(pj))
