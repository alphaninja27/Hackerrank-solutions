def cavityMap(grid):
    # Write your code here
    n=len(grid)
    c=0
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1] and grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j]:
                p=list(grid[i])
                p[j]='X'
                grid[i]=''.join(p)
    return grid
